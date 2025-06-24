# The Malaria Prediction Initiative: Saving Lives Through Data-Driven Prevention in Nigeria

## 1. Project Title & Overview

**Project Title:** "The Malaria Prediction Initiative: Saving Lives Through Data-Driven Prevention in Nigeria"

You are a Data Analyst for the Nigerian Ministry of Health, helping to predict when and where malaria outbreaks are most likely to occur. Your job is to analyze health data, climate patterns, and demographics to identify high-risk areas and timing for prevention campaigns.

You'll use WHO health data and climate information to build models that predict malaria cases, identify the most important factors causing outbreaks, and recommend when and where to deploy prevention resources. This project shows how data science can help save lives through better public health planning.

## 2. Background & Context

Malaria remains one of Nigeria's biggest health challenges, causing over 97 million cases and 300,000 deaths annually. The disease affects children and pregnant women most severely, particularly in rural areas with limited healthcare access.

Climate factors like rainfall, temperature, and humidity strongly influence mosquito breeding and malaria transmission. The Nigerian Ministry of Health needs to predict outbreak patterns to deploy bed nets, antimalarial drugs, and awareness campaigns more effectively across the country's 36 states.

Your analysis will help the Ministry allocate limited resources to the right places at the right times, potentially preventing thousands of cases and saving lives through data-driven prevention strategies.

## 3. Project Description

You will analyze malaria cases, climate data, and demographic information to predict outbreak patterns and recommend prevention strategies. Your tasks include: exploring relationships between climate factors and malaria cases, identifying high-risk states and time periods, building simple models to predict malaria cases, and analyzing which factors are most important for prevention planning.

You'll work with WHO health data containing malaria cases by state and year, climate data including rainfall and temperature, and basic demographic information. The analysis focuses on finding practical patterns that can guide public health decisions.

Use basic Python skills from the bootcamp: pandas for data analysis, matplotlib for charts, and simple machine learning models. The goal is to provide clear recommendations for where and when the Ministry should focus their malaria prevention efforts.

## 4. Data and Constraints

**Primary Dataset:** WHO Global Health Observatory malaria data for Nigeria by state (2015-2020), climate data including rainfall, temperature, and humidity from weather stations, and basic demographic data (population, urbanization levels). The dataset includes approximately 6 years of data across Nigeria's 36 states.

**Technical Constraints:** Use Python with pandas for data manipulation, matplotlib/seaborn for visualizations, and scikit-learn for basic machine learning. Focus on libraries covered in the bootcamp. Avoid complex epidemiological modeling - stick to simple prediction and correlation analysis.

**Business Constraints:** Consider Nigerian context - resource limitations, seasonal patterns, and state-level differences. Focus on practical recommendations that the Ministry can implement with available resources. Keep analysis understandable for public health officials who need to make policy decisions.

## 5. Expected Deliverables

**1. Jupyter Notebook Analysis (45% of grade)**
- Data cleaning and exploration of malaria cases, climate, and demographic data
- Analysis of relationships between climate factors and malaria cases
- State-by-state comparison showing high-risk areas
- Seasonal pattern analysis for optimal campaign timing
- Simple machine learning model to predict malaria cases
- Feature importance analysis showing key factors for prevention

**2. Public Health Strategy Report (40% of grade)**
- 4-8 page policy report with specific recommendations for the Ministry of Health
- Include identification of highest-risk states and time periods
- Climate-based early warning system recommendations
- Resource allocation strategies based on prediction models
- Prevention campaign timing and targeting suggestions
- Written for health policymakers who need actionable guidance

**3. Ministry Briefing Presentation (15% of grade)**
- A presentation slide for Ministry of Health leadership, that:
  - Focuses on key findings about malaria risk factors and patterns
  - Includes 3-4 clear visualizations showing risk areas and timing
  - Presents specific recommendations for prevention campaign planning
  - Explains how predictive models can improve health outcomes

All analysis should prioritize public health impact and practical implementation over complex technical methods.

## 6. Resources & Support

**Datasets:**
- WHO Global Health Observatory malaria statistics for Nigeria
- World Bank indicators on malaria and malaria incidences
- Nigerian climate data from meteorological stations
- State-level demographic data from National Bureau of Statistics
- Sample public health datasets for practice and validation
- [Optional] WHO Global Health Observatory via ghoclient Python library: `pip install ghoclient`

**Technical Resources:**
- Python libraries: pandas, matplotlib, seaborn, scikit-learn
- Jupyter Notebook templates for health data analysis
- Simple correlation and regression analysis tutorials
- Data visualization guides for public health presentations

**Background Materials:**
- Nigerian malaria control strategy documents
- Climate-health relationship research papers (simplified summaries)
- Public health data analysis best practices
- Case studies of successful malaria prediction programs from other countries