import pandas as pd
import numpy as np
import random

# Reproducibility (IMPORTANT for projects)
np.random.seed(42)
random.seed(42)

n = 100000

# Time range (monthly) ✅ FIXED HERE
months = pd.date_range(start="2020-01-01", end="2026-12-31", freq="ME")

states_districts = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik"],
    "Karnataka": ["Bangalore", "Mysore", "Hubli"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai"],
    "UP": ["Lucknow", "Kanpur", "Varanasi"],
    "Bihar": ["Patna", "Gaya"],
    "Delhi": ["New Delhi", "South Delhi"],
}

education_levels = [
    "No Education", "Primary", "Secondary",
    "Higher Secondary", "Graduate", "Postgraduate"
]

def get_covid_phase(year):
    if year == 2020:
        return "Shock"
    elif year == 2021:
        return "Recovery"
    elif year in [2022, 2023]:
        return "Stabilizing"
    else:
        return "Stable"

def job_market_index(year):
    base = {
        2020: 0.4,
        2021: 0.55,
        2022: 0.65,
        2023: 0.7,
        2024: 0.75,
        2025: 0.8,
        2026: 0.78
    }   
    noise = np.random.normal(0, 0.05)
    return max(0.2, min(base[year] + noise, 1))

data = []

state_list = list(states_districts.keys())

for i in range(n):
    date = random.choice(months)
    year = date.year
    month = date.month
    
    state = random.choice(state_list)
    district = random.choice(states_districts[state])
    
    age = np.random.randint(18, 60)
    gender = np.random.choice(["Male", "Female", "Other"], p=[0.51, 0.48, 0.01])
    area = np.random.choice(["Urban", "Rural"], p=[0.6, 0.4])
    edu = random.choice(education_levels)
    
    # Skill score
    edu_score_map = {
        "No Education": 0.2,
        "Primary": 0.3,
        "Secondary": 0.5,
        "Higher Secondary": 0.6,
        "Graduate": 0.75,
        "Postgraduate": 0.85
    }
    
    skill_score = edu_score_map[edu] + np.random.normal(0, 0.05)
    skill_score = max(0, min(skill_score, 1))  # clamp
    
    covid_phase = get_covid_phase(year)
    market_index = job_market_index(year)
    
    # Improved probability model
    prob = (0.5 * market_index) + (0.5 * skill_score)
    
    if age <= 25:
        prob *= 0.75
    elif age >= 50:
        prob *= 0.85
        
    if gender == "Female":
        prob *= 0.92
        
    if area == "Rural":
        prob *= 1.05
    
    prob = max(0.05, min(prob, 0.95))
    
    rand = np.random.rand()
    
    if rand < prob:
        status = "Employed"
    elif rand < prob + 0.12:
        status = "Underemployed"
    else:
        status = "Unemployed"
    
    months_unemp = 0
    if status == "Unemployed":
        months_unemp = np.random.randint(3, 24)
    elif status == "Underemployed":
        months_unemp = np.random.randint(1, 12)
    
    data.append([
        i+1, date, year, month, state, district,
        age, gender, area, edu,
        round(skill_score, 2),
        covid_phase,
        round(market_index, 2),
        round(prob, 2),
        status,
        months_unemp
    ])

df = pd.DataFrame(data, columns=[
    "person_id", "date", "year", "month",
    "state", "district", "age", "gender",
    "urban_rural", "education_level",
    "skill_score", "covid_phase",
    "job_market_index", "employment_probability",
    "employment_status", "months_unemployed"
])

df.to_csv("advanced_india_unemployment_2020_2026.csv", index=False)

print("✅ Advanced dataset ready!")  