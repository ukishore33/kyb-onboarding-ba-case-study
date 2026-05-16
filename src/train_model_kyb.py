"""
KYC/KYB Entity Risk Scoring Engine - ML Model Training
Author: Kishore U.
Description: Trains Gradient Boosting + Random Forest for KYB entity risk classification
             Outputs scored entities and model metrics JSON for dashboard
"""

import pandas as pd
import numpy as np
import json
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    classification_report, confusion_matrix,
    roc_auc_score, precision_score, recall_score, f1_score, accuracy_score
)

def train_model():
    df = pd.read_csv("/Users/kishoreu/Documents/GitHub/KYC-KYB-Entity-Risk-Scoring-Engine/data/entities.csv")

    # ── FEATURE ENGINEERING ────────────────────────────────────────────────
    le = LabelEncoder()
    df["jurisdiction_risk_enc"] = le.fit_transform(df["jurisdiction_risk"])
    df["sector_risk_enc"]       = le.fit_transform(df["sector_risk"])
    df["entity_type_enc"]       = le.fit_transform(df["entity_type"])

    df["reg_age_years"]      = (df["registration_age_days"] / 365).round(2)
    df["ubo_opacity_score"]  = (
        (1 - df["ubo_disclosed"]) * 40 +
        df["ubo_pep_flag"] * 30 +
        df["ubo_sanctions_flag"] * 30
    )
    df["structure_complexity"] = (
        df["shell_company_flag"] * 30 +
        df["complex_structure_flag"] * 25 +
        np.log1p(df["num_subsidiaries"]) * 5 +
        df["layering_depth"] * 5
    )
    df["financial_opacity"]  = np.log1p(df["income_turnover_gap"])
    df["alert_signal_count"] = (
        df["worldcheck_hit"] +
        df["adverse_media_flag"] +
        df["shell_company_flag"] +
        df["complex_structure_flag"] +
        df["dormant_flag"] +
        df["multi_directorship_flag"] +
        (1 - df["docs_complete"])
    )

    FEATURES = [
        "jurisdiction_risk_enc", "sector_risk_enc", "entity_type_enc",
        "ubo_disclosed", "ubo_pep_flag", "ubo_sanctions_flag",
        "entity_sanctions_flag", "worldcheck_hit",
        "shell_company_flag", "complex_structure_flag",
        "num_subsidiaries", "layering_depth",
        "adverse_media_flag", "adverse_media_count",
        "dormant_flag", "multi_directorship_flag", "director_company_count",
        "docs_complete", "reg_age_years",
        "ubo_opacity_score", "structure_complexity",
        "financial_opacity", "alert_signal_count",
    ]

    X = df[FEATURES]
    y = df["sar_label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # ── GRADIENT BOOSTING (PRIMARY) ────────────────────────────────────────
    gb = GradientBoostingClassifier(
        n_estimators=300, learning_rate=0.05,
        max_depth=4, subsample=0.8,
        min_samples_leaf=10, random_state=42
    )
    gb.fit(X_train, y_train)
    y_pred_gb  = gb.predict(X_test)
    y_proba_gb = gb.predict_proba(X_test)[:, 1]

    # ── RANDOM FOREST (COMPARISON) ─────────────────────────────────────────
    rf = RandomForestClassifier(
        n_estimators=200, max_depth=8,
        class_weight="balanced", random_state=42
    )
    rf.fit(X_train, y_train)
    y_pred_rf  = rf.predict(X_test)
    y_proba_rf = rf.predict_proba(X_test)[:, 1]

    # ── METRICS ───────────────────────────────────────────────────────────
    def get_metrics(y_true, y_pred, y_proba):
        return {
            "accuracy":  round(float(accuracy_score(y_true, y_pred)), 4),
            "precision": round(float(precision_score(y_true, y_pred)), 4),
            "recall":    round(float(recall_score(y_true, y_pred)), 4),
            "f1_score":  round(float(f1_score(y_true, y_pred)), 4),
            "roc_auc":   round(float(roc_auc_score(y_true, y_proba)), 4),
        }

    metrics = {
        "gradient_boosting": get_metrics(y_test, y_pred_gb, y_proba_gb),
        "random_forest":     get_metrics(y_test, y_pred_rf, y_proba_rf),
    }

    # Cross-validation AUC
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    cv_auc = cross_val_score(gb, X, y, cv=cv, scoring="roc_auc")
    metrics["gradient_boosting"]["cv_auc_mean"] = round(float(cv_auc.mean()), 4)
    metrics["gradient_boosting"]["cv_auc_std"]  = round(float(cv_auc.std()), 4)

    # Feature importances
    feat_imp = sorted(
        zip(FEATURES, gb.feature_importances_),
        key=lambda x: x[1], reverse=True
    )
    feature_importance = [
        {"feature": f, "importance": round(float(v), 4)}
        for f, v in feat_imp
    ]

    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred_gb).tolist()

    # ── SCORE FULL DATASET ─────────────────────────────────────────────────
    df["ml_risk_score"] = (gb.predict_proba(X[FEATURES])[:, 1] * 100).round(1)

    def risk_tier(score):
        if score >= 65: return "High"
        elif score >= 35: return "Medium"
        else: return "Low"

    df["ml_risk_tier"]  = df["ml_risk_score"].apply(risk_tier)
    df["ml_alert"]      = (df["ml_risk_score"] >= 65).astype(int)

    df.to_csv("//Users/kishoreu/Documents/GitHub/KYC-KYB-Entity-Risk-Scoring-Engine/data/entities_scored.csv", index=False)

    # ── RISK TIER BREAKDOWN BY SECTOR ─────────────────────────────────────
    sector_breakdown = (
        df.groupby(["sector", "ml_risk_tier"])
        .size().reset_index(name="count")
        .pivot(index="sector", columns="ml_risk_tier", values="count")
        .fillna(0).astype(int).reset_index()
        .rename_axis(None, axis=1)
    ).to_dict(orient="records")

    # ── JURISDICTION BREAKDOWN ─────────────────────────────────────────────
    juris_breakdown = (
        df[df["ml_alert"] == 1]
        .groupby("jurisdiction")
        .size().reset_index(name="count")
        .sort_values("count", ascending=False)
        .head(10)
        .to_dict(orient="records")
    )

    # ── SUMMARY ───────────────────────────────────────────────────────────
    summary = {
        "total_entities":        int(len(df)),
        "high_risk_entities":    int((df["ml_risk_tier"] == "High").sum()),
        "medium_risk_entities":  int((df["ml_risk_tier"] == "Medium").sum()),
        "low_risk_entities":     int((df["ml_risk_tier"] == "Low").sum()),
        "worldcheck_hits":       int(df["worldcheck_hit"].sum()),
        "pep_flagged":           int(df["ubo_pep_flag"].sum()),
        "sanctions_flagged":     int((df["ubo_sanctions_flag"] | df["entity_sanctions_flag"]).sum()),
        "shell_companies":       int(df["shell_company_flag"].sum()),
        "adverse_media":         int(df["adverse_media_flag"].sum()),
        "docs_incomplete":       int((df["docs_complete"] == 0).sum()),
        "offshore_jurisdictions":int((df["jurisdiction_risk"] == "High").sum()),
    }

    output = {
        "metrics":            metrics,
        "feature_importance": feature_importance,
        "confusion_matrix":   cm,
        "summary":            summary,
        "sector_breakdown":   sector_breakdown,
        "juris_breakdown":    juris_breakdown,
    }

    with open("/Users/kishoreu/Documents/GitHub/KYC-KYB-Entity-Risk-Scoring-Engine/data/model_results.json", "w") as f:
        json.dump(output, f, indent=2)

    print("✅ Model training complete!")
    print(f"   Gradient Boosting → AUC: {metrics['gradient_boosting']['roc_auc']} | F1: {metrics['gradient_boosting']['f1_score']} | CV-AUC: {metrics['gradient_boosting']['cv_auc_mean']} ±{metrics['gradient_boosting']['cv_auc_std']}")
    print(f"   Random Forest     → AUC: {metrics['random_forest']['roc_auc']} | F1: {metrics['random_forest']['f1_score']}")
    print(f"   High-risk alerts: {summary['high_risk_entities']} | Medium: {summary['medium_risk_entities']} | Low: {summary['low_risk_entities']}")

    return output

if __name__ == "__main__":
    train_model()
