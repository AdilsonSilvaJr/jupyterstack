# Project Stack Labs - Team Jupyter

Exploring a dataset on kaggle "Diabetes Health Indicators Dataset"

https://www.kaggle.com/alexteboul/diabetes-health-indicators-dataset

## All Credits for Alex Teboul for doing the pre-processing:
Kaggle: https://www.kaggle.com/alexteboul

### Selected Subset of Features from BRFSS 2015

**BRFSS 2015 Codebook:** https://www.cdc.gov/brfss/annual_data/2015/pdf/codebook15_llcp.pdf

**Relevant Research Paper using BRFSS for Diabetes ML:** https://www.cdc.gov/pcd/issues/2019/19_0109.htm

The **selected features** from the BRFSS 2015 dataset are:

**Response Variable / Dependent Variable:**
*   (Ever told) you have diabetes (If "Yes" and respondent is female, ask "Was this only when you were pregnant?". If Respondent says pre-diabetes or borderline diabetes, use response code 4.) --> DIABETE3

**Independent Variables:**

**High Blood Pressure**
*   Adults who have been told they have high blood pressure by a doctor, nurse, or other health professional --> _RFHYPE5

**High Cholesterol**
*   Have you EVER been told by a doctor, nurse or other health professional that your blood cholesterol is high? --> TOLDHI2
*   Cholesterol check within past five years --> _CHOLCHK

**BMI**
*   Body Mass Index (BMI) --> _BMI5

**Smoking**
*   Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes] --> SMOKE100

**Other Chronic Health Conditions**
*   (Ever told) you had a stroke. --> CVDSTRK3
*   Respondents that have ever reported having coronary heart disease (CHD) or myocardial infarction (MI) --> _MICHD

**Physical Activity**
*   Adults who reported doing physical activity or exercise during the past 30 days other than their regular job --> _TOTINDA

**Diet**
*   Consume Fruit 1 or more times per day --> _FRTLT1
*   Consume Vegetables 1 or more times per day --> _VEGLT1

**Alcohol Consumption**
*   Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week) --> _RFDRHV5

**Health Care**
*   Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs, or government plans such as Medicare, or Indian Health Service?  --> HLTHPLN1
*   Was there a time in the past 12 months when you needed to see a doctor but could not because of cost? --> MEDCOST

**Health General and Mental Health**
*   Would you say that in general your health is: --> GENHLTH
*   Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good? --> MENTHLTH
*   Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? --> PHYSHLTH
*   Do you have serious difficulty walking or climbing stairs? --> DIFFWALK

**Demographics**
*   Indicate sex of respondent. --> SEX
*   Fourteen-level age category --> _AGEG5YR
*   What is the highest grade or year of school you completed? --> EDUCA
*   Is your annual household income from all sources: (If respondent refuses at any income level, code "Refused.") --> INCOME2
