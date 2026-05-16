"""
KYC/KYB Entity Risk Scoring Engine - Synthetic Entity Generator
Author: Kishore U.
Description: Generates realistic synthetic business entity data with KYC/KYB red flags
             Simulates data typically sourced from OpenCorporates, EDGAR, World-Check
"""

import pandas as pd
import numpy as np
import json
import random
from datetime import datetime, timedelta

np.random.seed(99)
random.seed(99)

# ── REFERENCE DATA ─────────────────────────────────────────────────────────
HIGH_RISK_JURISDICTIONS = ["British Virgin Islands", "Cayman Islands", "Panama",
                            "Seychelles", "Marshall Islands", "Vanuatu", "Belize"]
MEDIUM_RISK_JURISDICTIONS = ["Cyprus", "Malta", "Hong Kong", "Dubai", "Singapore"]
LOW_RISK_JURISDICTIONS = ["India", "USA", "UK", "Germany", "Australia", "Japan", "Canada"]

HIGH_RISK_SECTORS = ["Cryptocurrency", "Arms & Defense", "Gambling", "Mining", "Oil & Gas Trading"]
MEDIUM_RISK_SECTORS = ["Real Estate", "Import/Export", "Hospitality", "Money Services", "Pawnbroking"]
LOW_RISK_SECTORS = ["IT Services", "Healthcare", "Education", "Retail", "Manufacturing", "Logistics"]

ENTITY_TYPES = ["Private Limited", "LLP", "Public Limited", "Partnership", "Sole Proprietor", "Trust"]
BANK_NAMES = ["HDFC Bank", "ICICI Bank", "Axis Bank", "Kotak Mahindra", "Yes Bank",
              "Standard Chartered", "Citibank", "Deutsche Bank", "Barclays", "HSBC"]

FIRST_NAMES = ["Rajesh", "Priya", "Mohammed", "Sunita", "Arun", "Deepika",
               "John", "Sarah", "Wei", "Fatima", "Carlos", "Ananya"]
LAST_NAMES  = ["Kumar", "Sharma", "Patel", "Singh", "Mehta", "Reddy",
               "Chen", "Williams", "Al-Farsi", "Gupta", "Nair", "Iyer"]

def random_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"

def random_date(start_yr=2005, end_yr=2024):
    start = datetime(start_yr, 1, 1)
    end   = datetime(end_yr, 12, 31)
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime("%Y-%m-%d")

# ── GENERATOR ──────────────────────────────────────────────────────────────
def generate_entities(n=1000):
    records = []

    for i in range(n):
        is_high_risk = random.random() < 0.20
        is_medium_risk = (not is_high_risk) and (random.random() < 0.30)

        entity_id   = f"ENT{i+1:05d}"
        entity_name = f"{random.choice(LAST_NAMES)} {random.choice(['Holdings','Ventures','Solutions','Trading','Enterprises','Capital','Group','Consulting'])} {'Ltd' if random.random()>0.4 else 'LLP'}"
        entity_type = random.choice(ENTITY_TYPES)
        reg_date    = random_date(2005, 2023)
        reg_number  = f"REG{random.randint(100000,999999)}"

        # Jurisdiction
        if is_high_risk and random.random() < 0.7:
            jurisdiction = random.choice(HIGH_RISK_JURISDICTIONS)
            jurisdiction_risk = "High"
        elif is_medium_risk and random.random() < 0.5:
            jurisdiction = random.choice(MEDIUM_RISK_JURISDICTIONS)
            jurisdiction_risk = "Medium"
        else:
            jurisdiction = random.choice(LOW_RISK_JURISDICTIONS)
            jurisdiction_risk = "Low"

        # Sector
        if is_high_risk and random.random() < 0.6:
            sector = random.choice(HIGH_RISK_SECTORS)
            sector_risk = "High"
        elif is_medium_risk and random.random() < 0.5:
            sector = random.choice(MEDIUM_RISK_SECTORS)
            sector_risk = "Medium"
        else:
            sector = random.choice(LOW_RISK_SECTORS)
            sector_risk = "Low"

        # UBO details
        ubo_count       = random.randint(1, 2) if not is_high_risk else random.randint(3, 6)
        ubo_disclosed   = 0 if (is_high_risk and random.random() < 0.55) else 1
        ubo_pep_flag    = 1 if (is_high_risk and random.random() < 0.30) else 0
        ubo_sanctions   = 1 if (is_high_risk and random.random() < 0.25) else 0
        ubo_name        = random_name()
        ubo_nationality = random.choice(["Indian", "British", "UAE", "Cayman", "American", "Nigerian", "Russian"])

        # Shell / Complexity indicators
        shell_company_flag      = 1 if (is_high_risk and random.random() < 0.55) else 0
        complex_structure_flag  = 1 if (is_high_risk and random.random() < 0.45) else 0
        num_subsidiaries        = random.randint(5, 20) if is_high_risk else random.randint(0, 4)
        layering_depth          = random.randint(3, 6) if is_high_risk else random.randint(1, 2)

        # Adverse media
        adverse_media_flag  = 1 if (is_high_risk and random.random() < 0.40) else 0
        adverse_media_count = random.randint(3, 12) if adverse_media_flag else 0

        # Financial indicators
        annual_turnover_cr = round(random.uniform(0.5, 5), 2) if is_high_risk and random.random() < 0.4 else round(random.uniform(5, 500), 2)
        declared_income_cr = round(annual_turnover_cr * random.uniform(0.1, 0.4), 2)
        income_turnover_gap = round(abs(annual_turnover_cr - declared_income_cr * 3), 2)

        # Dormancy & registration age
        reg_age_days = (datetime.now() - datetime.strptime(reg_date, "%Y-%m-%d")).days
        dormant_flag = 1 if (reg_age_days < 180 and is_high_risk) else 0

        # Multiple directorships
        director_name           = random_name()
        multi_directorship_flag = 1 if (is_high_risk and random.random() < 0.40) else 0
        director_company_count  = random.randint(5, 20) if multi_directorship_flag else random.randint(1, 3)

        # Document completeness
        docs_complete = 0 if (is_high_risk and random.random() < 0.45) else 1

        # Sanctions & watchlist
        entity_sanctions_flag = 1 if (is_high_risk and random.random() < 0.20) else 0
        worldcheck_hit        = 1 if (ubo_sanctions or entity_sanctions_flag) else 0

        # Compute rule-based risk score
        score = 0
        if jurisdiction_risk == "High":   score += 30
        elif jurisdiction_risk == "Medium": score += 15
        if sector_risk == "High":          score += 25
        elif sector_risk == "Medium":      score += 12
        if not ubo_disclosed:              score += 20
        if ubo_pep_flag:                   score += 20
        if ubo_sanctions or entity_sanctions_flag: score += 25
        if shell_company_flag:             score += 20
        if complex_structure_flag:         score += 15
        if adverse_media_flag:             score += 15
        if dormant_flag:                   score += 10
        if multi_directorship_flag:        score += 10
        if not docs_complete:              score += 15
        if worldcheck_hit:                 score += 25
        score = min(score, 100)

        # Ground truth label
        sar_label = 1 if is_high_risk else 0

        records.append({
            "entity_id":              entity_id,
            "entity_name":            entity_name,
            "entity_type":            entity_type,
            "registration_number":    reg_number,
            "registration_date":      reg_date,
            "registration_age_days":  reg_age_days,
            "jurisdiction":           jurisdiction,
            "jurisdiction_risk":      jurisdiction_risk,
            "sector":                 sector,
            "sector_risk":            sector_risk,
            "ubo_name":               ubo_name,
            "ubo_nationality":        ubo_nationality,
            "ubo_count":              ubo_count,
            "ubo_disclosed":          ubo_disclosed,
            "ubo_pep_flag":           ubo_pep_flag,
            "ubo_sanctions_flag":     ubo_sanctions,
            "entity_sanctions_flag":  entity_sanctions_flag,
            "worldcheck_hit":         worldcheck_hit,
            "shell_company_flag":     shell_company_flag,
            "complex_structure_flag": complex_structure_flag,
            "num_subsidiaries":       num_subsidiaries,
            "layering_depth":         layering_depth,
            "adverse_media_flag":     adverse_media_flag,
            "adverse_media_count":    adverse_media_count,
            "annual_turnover_cr":     annual_turnover_cr,
            "declared_income_cr":     declared_income_cr,
            "income_turnover_gap":    income_turnover_gap,
            "dormant_flag":           dormant_flag,
            "director_name":          director_name,
            "multi_directorship_flag": multi_directorship_flag,
            "director_company_count": director_company_count,
            "docs_complete":          docs_complete,
            "rule_risk_score":        score,
            "sar_label":              sar_label,
        })

    df = pd.DataFrame(records)
    df.to_csv("/Users/kishoreu/Documents/GitHub/KYC-KYB-Entity-Risk-Scoring-Engine/data/entities.csv", index=False)
    print(f"✅ Generated {n} entities | High-Risk: {df['sar_label'].sum()} ({df['sar_label'].mean()*100:.1f}%)")
    return df

if __name__ == "__main__":
    generate_entities()
