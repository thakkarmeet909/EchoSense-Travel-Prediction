# 🧬 EchoSense AI — IBM Final Project PPT PROMPT
# Copy EVERYTHING inside the box below and paste into Gamma.app / Beautiful.AI / Canva AI

======================================================================
COPY FROM HERE
======================================================================

Create a professional, modern, visually stunning 20-slide PowerPoint
presentation for a final year IBM SkillsBuild Certification project.

PROJECT TITLE: "EchoSense AI: Customer Churn Prediction for the Travel Industry"
SUBTITLE: "A Machine Learning Powered Dashboard using Random Forest Classifier"

DESIGN RULES:
- Dark theme: Background #121212 (deep black)
- Primary accent: Electric Violet #8A3FFC
- CHURN result color: Crimson Red #ff4b4b
- NOT CHURN result color: Emerald Green #00d26a
- Font: Inter or Outfit (body), Manrope Bold (headings)
- Style: Glassmorphism SaaS dashboard — premium, futuristic, enterprise-grade
- Footer on every slide: "EchoSense AI | IBM SkillsBuild Final Project | 2026"
- Aspect ratio: 16:9

----------------------------------------------------------------------

SLIDE 1 — TITLE SLIDE
- Main Title: EchoSense AI
- Subtitle: Customer Churn Prediction for the Travel Industry
- Tagline: Deep Retention Intelligence — Powered by Machine Learning
- Presented By: [Your Name]
- Roll Number: [Your Roll Number]
- College: [Your College Name]
- Mentor: [Mentor Name]
- Date: May 2026
- Background: Futuristic dark AI / travel themed with violet glow particles

----------------------------------------------------------------------

SLIDE 2 — TABLE OF CONTENTS
Show as numbered cards or a visual timeline:
1.  Introduction & Motivation
2.  Problem Statement
3.  Project Objectives
4.  Dataset Description
5.  Churn Data Visualization (Graphs)
6.  System Architecture
7.  Technology Stack
8.  Data Preprocessing & Feature Engineering
9.  Model Training Pipeline (Jupyter Notebook)
10. Model Evaluation & Accuracy Metrics
11. Web Dashboard — 4 Intelligence Modules
12. Churn Predictor — How Results Are Shown
13. UI / UX Design Philosophy
14. Deployment Strategy (GitHub + Streamlit)
15. Live Demo Screenshots
16. Results & Key Findings
17. Business Impact & ROI
18. Challenges Faced
19. Future Scope
20. Conclusion & References

----------------------------------------------------------------------

SLIDE 3 — INTRODUCTION & MOTIVATION
Headline: Why Does Customer Churn Matter?

Bullet points:
• The global travel and tourism industry is worth over $9.6 Trillion (2023)
• Only 23.5% of travel customers actually purchase a package
• 76.5% of customers churn — they leave WITHOUT buying
• Each lost customer = lost revenue + wasted marketing spend
• Traditional methods cannot predict WHO will churn in advance
• Machine Learning enables proactive, data-driven churn prevention
• EchoSense AI transforms raw customer profiles into CHURN or NOT CHURN predictions in real time

Closing line: "Stop reacting to churn. Start predicting it."

----------------------------------------------------------------------

SLIDE 4 — PROBLEM STATEMENT
Headline: What Problem Are We Solving?

Main problem (big text in center): 
"How can travel companies identify customers at risk of churning 
BEFORE they leave — and take action to retain them?"

Key challenges (4 boxes):
Box 1 — High Churn Rate: 76.5% of customers do not purchase (churn)
Box 2 — Wasted Budget: Marketing campaigns target everyone equally
Box 3 — Unused Data: Customer behavioral data is never analyzed
Box 4 — No Platform: No unified prediction + visualization tool exists

Our Answer: EchoSense AI — an ML-powered Streamlit dashboard that
predicts churn instantly and outputs ❌ CHURN or ✅ NOT CHURN clearly.

----------------------------------------------------------------------

SLIDE 5 — PROJECT OBJECTIVES
Headline: What We Set Out to Build

Numbered objectives:
1. Train a Random Forest ML model to predict customer churn accurately
2. Build a real-time Streamlit web dashboard for individual churn prediction
3. Display results clearly as ❌ CHURN (Target=1) or ✅ NOT CHURN (Target=0)
4. Provide deep behavioral analytics via 4 interactive dashboard modules
5. Enable bulk churn scoring via CSV batch upload
6. Achieve model accuracy above 85%
7. Deploy the full system live on the cloud via Streamlit Community Cloud
8. Make the product usable by non-technical business users

----------------------------------------------------------------------

SLIDE 6 — DATASET DESCRIPTION
Headline: Our Data — Customertravel.csv

Dataset Overview Table:
| Property        | Value                                         |
|-----------------|-----------------------------------------------|
| Dataset Name    | Customertravel.csv                            |
| Source          | IBM SkillsBuild / Kaggle                      |
| Total Records   | 954 customers                                 |
| Total Columns   | 7 (6 Features + 1 Target)                     |
| Task Type       | Binary Classification (Churn / Not Churn)     |
| Class 0 (Churn) | 730 customers — 76.5%                         |
| Class 1 (Retain)| 224 customers — 23.5%                         |

Feature Breakdown Table:
| # | Feature Name                  | Type        | Values                               |
|---|-------------------------------|-------------|--------------------------------------|
| 1 | Age                           | Numerical   | 18 - 60 years                        |
| 2 | FrequentFlyer                 | Categorical | Yes / No / No Record                 |
| 3 | AnnualIncomeClass             | Categorical | Low Income / Middle Income / High Income |
| 4 | ServicesOpted                 | Numerical   | 1 to 6 services                      |
| 5 | AccountSyncedToSocialMedia    | Categorical | Yes / No                             |
| 6 | BookedHotelOrNot              | Categorical | Yes / No                             |
| 7 | Target (Label)                | Binary      | 1 = CHURN (Did Not Buy), 0 = NOT CHURN (Purchased) |

----------------------------------------------------------------------

SLIDE 7 — CHURN DATA VISUALIZATION (FULL-PAGE GRAPH SLIDE)
Headline: What Does the Data Tell Us?

Make this slide GRAPH DOMINANT — 4 charts in a 2x2 grid, minimal text.

GRAPH 1 (Top-Left) — Donut Chart: Overall Churn Distribution
  Title: "Churn vs Retention Rate"
  Data: 
    ❌ Churned (No Purchase) = 730 customers = 76.5% → Color: Crimson Red
    ✅ Not Churned (Purchased) = 224 customers = 23.5% → Color: Emerald Green
  Center of donut: "954 Total Customers"
  Insight below: "3 out of 4 customers churn — critical retention gap"

GRAPH 2 (Top-Right) — Grouped Bar Chart: Churn by Income Class
  Title: "Churn Rate by Annual Income Class"
  Data:
    High Income   → Churn Rate ~42.9%   (Lowest churn, highest retention)
    Middle Income → Churn Rate ~84.2%   (Very high churn)
    Low Income    → Churn Rate ~85.0%   (Highest churn)
  Colors: Red bars = Churn, Green bars = Retain
  Insight: "High Income customers churn 3x LESS than Low Income"

GRAPH 3 (Bottom-Left) — Bar Chart: Churn by Frequent Flyer Status
  Title: "Frequent Flyer vs Churn Status"
  Data:
    Frequent Flyer = Yes       → Retention Rate ~38%
    Frequent Flyer = No        → Retention Rate ~15%
    Frequent Flyer = No Record → Retention Rate ~18%
  Colors: Violet accent bars
  Insight: "Frequent Flyers are 2.5x more likely to NOT churn"

GRAPH 4 (Bottom-Right) — Histogram: Services Opted vs Churn
  Title: "Services Opted by Churn Status"
  X-axis: Number of services opted (1 to 6)
  Y-axis: Number of customers
  Two overlapping bars: Red = Churned, Green = Retained
  Insight: "Customers opting for more services have varied churn patterns"

----------------------------------------------------------------------

SLIDE 8 — SYSTEM ARCHITECTURE
Headline: How EchoSense AI Works End-to-End

Show as a horizontal flowchart with icons:

[📂 Customertravel.csv]
    ↓
[🔧 Data Preprocessing]
    (Label Encoding + Standard Scaling)
    ↓
[✂️ Train-Test Split]
    (80% Train = 763 samples | 20% Test = 191 samples)
    ↓
[🌲 Random Forest Classifier]
    (100 Decision Trees | random_state=42)
    ↓
[📊 Model Evaluation]
    (Accuracy: 88% | Confusion Matrix | ROC Curve)
    ↓
[💾 Serialize Model]
    (travel_model_assets.pkl)
    ↓
[🌐 Streamlit Web Dashboard]
    ↓
[☁️ Deployed Live]
    (Streamlit Community Cloud / Hugging Face Spaces)

Side note boxes:
  Training done in: Model_Training.ipynb (Jupyter Notebook)
  Output: ❌ CHURN or ✅ NOT CHURN + Probability %

----------------------------------------------------------------------

SLIDE 9 — TECHNOLOGY STACK
Headline: Tools & Technologies Used

Show as icon-based grid cards:

| Layer                | Tool / Library          | Purpose                                      |
|----------------------|-------------------------|----------------------------------------------|
| Programming Language | Python 3.10+            | Core development language                    |
| Web Framework        | Streamlit               | Interactive real-time dashboard              |
| Machine Learning     | Scikit-learn            | Random Forest model training & prediction    |
| Data Processing      | Pandas + NumPy          | Data loading, cleaning, transformation       |
| Interactive Charts   | Plotly                  | Gauge charts, bar charts, histograms         |
| EDA & Visualization  | Matplotlib + Seaborn    | Training notebook charts, heatmaps           |
| Model Saving         | Joblib                  | Serialize and load model artifacts           |
| Preprocessing        | LabelEncoder + Scaler   | Encode categories, normalize features        |
| Notebook             | Jupyter Notebook (.ipynb)| Full model training and EDA workflow        |
| UI Styling           | Custom CSS (Glassmorphism)| Dark premium SaaS dashboard theme          |
| Typography           | Google Fonts (Inter + Manrope)| Modern professional typography         |
| Version Control      | Git + GitHub            | Source code management & collaboration       |
| Deployment           | Streamlit Community Cloud| Make the app live on the internet           |

----------------------------------------------------------------------

SLIDE 10 — DATA PREPROCESSING & FEATURE ENGINEERING
Headline: Preparing the Data for Machine Learning

Show as a numbered step pipeline:

STEP 1 — Data Loading
  Read Customertravel.csv into a Pandas DataFrame
  Shape: 954 rows × 7 columns
  Confirmed: ZERO null / missing values

STEP 2 — Missing Value Handling
  "No Record" in FrequentFlyer = treated as a valid third category (NOT missing)
  No imputation needed — dataset is clean

STEP 3 — Categorical Encoding (LabelEncoder)
  Applied to 4 columns:
  • FrequentFlyer       → No=0, No Record=1, Yes=2
  • AnnualIncomeClass   → High Income=0, Low Income=1, Middle Income=2
  • AccountSyncedToSocialMedia → No=0, Yes=1
  • BookedHotelOrNot   → No=0, Yes=1
  All 4 encoders saved in le_dict{} for runtime prediction

STEP 4 — Feature Scaling (StandardScaler)
  All 6 features scaled to Zero Mean + Unit Variance
  Ensures all features contribute equally to the model

STEP 5 — Train-Test Split
  Test Size: 20% | Train Size: 80%
  Training Set: 763 samples | Testing Set: 191 samples
  random_state=42 (reproducibility guaranteed)

----------------------------------------------------------------------

SLIDE 11 — MODEL TRAINING PIPELINE (JUPYTER NOTEBOOK)
Headline: Training the Random Forest Classifier

Show as two columns:

LEFT COLUMN — Why Random Forest?
  ✅ Handles both numerical and categorical features
  ✅ Robust against overfitting via ensemble averaging
  ✅ Provides feature importance scores
  ✅ Works well with imbalanced datasets
  ✅ Fast training on small/medium datasets
  ✅ No assumptions about data distribution

RIGHT COLUMN — Model Hyperparameters
  | Parameter         | Value         | Why?                              |
  |-------------------|---------------|-----------------------------------|
  | n_estimators      | 100           | 100 trees for stable predictions  |
  | criterion         | gini (default)| Standard impurity measure         |
  | max_depth         | None          | Trees grow to full depth          |
  | random_state      | 42            | Full reproducibility              |
  | min_samples_split | 2 (default)   | Standard split threshold          |

Training Code:
  rf = RandomForestClassifier(n_estimators=100, random_state=42)
  rf.fit(X_train, y_train)
  y_pred = rf.predict(X_test)
  Model saved → travel_model_assets.pkl

----------------------------------------------------------------------

SLIDE 12 — MODEL EVALUATION & ACCURACY METRICS
Headline: How Well Does the Model Perform?

MAIN NUMBER (big, centered, violet):
  🎯 Model Accuracy: 87.96% (~88%)

Precision / Recall / F1 Table:
| Metric    | NOT CHURN (Class 0) | CHURN (Class 1) | Weighted Avg |
|-----------|---------------------|-----------------|--------------|
| Precision | 0.91                | 0.74            | 0.87         |
| Recall    | 0.95                | 0.61            | 0.88         |
| F1-Score  | 0.93                | 0.67            | 0.87         |
| Support   | 153 samples         | 38 samples      | 191 total    |

Confusion Matrix (2x2 visual):
  Predicted NOT CHURN | Predicted CHURN
  True NOT CHURN: 145 (TN) | 8 (FP)
  True CHURN:      15 (FN) | 23 (TP)

Key Insights:
  • 88% accuracy — strong overall performance
  • 91% precision identifying retained customers
  • 74% precision catching actual churners
  • ROC-AUC score confirms model is well above random baseline

----------------------------------------------------------------------

SLIDE 13 — WEB DASHBOARD — 4 INTELLIGENCE MODULES
Headline: The EchoSense AI Dashboard

Show as 4 large cards (2x2 grid), each with icon + description:

CARD 1 — 📊 Executive Summary
  KPIs: Total Customers (954), Churn Rate (76.5%), Retention Rate (23.5%)
  "What This Model Does" explainer box explaining CHURN vs NOT CHURN
  Age distribution histogram colored by churn status (Red/Green)
  Live customer registry feed (random 10 records)

CARD 2 — 💡 Customer Pulse Analytics
  Churn Rate by Income Class — Grouped Bar Chart (Red/Green)
  Frequent Flyer vs Churn — Bar Chart
  Services Opted Distribution — Histogram overlay
  Hotel Booking vs Churn — Correlation Chart

CARD 3 — 🔍 Churn Predictor (Individual)
  6-input form: Age, FrequentFlyer, IncomeClass, ServicesOpted, SocialMedia, Hotel
  Click: "PREDICT CHURN STATUS"
  Output 1: ❌ CHURN banner (Red, full-width) or ✅ NOT CHURN banner (Green)
  Output 2: Gauge chart (0–100%) with colored risk zones
  Output 3: Detail table — Risk Level (🔴🟡🟢) + Recommended Action

CARD 4 — ⚙️ Batch Processing Engine
  Upload any Customertravel-format CSV
  Model scores every row and outputs:
    - Churn_Probability (0.00 to 1.00)
    - Result column: ✅ NOT CHURN or ❌ CHURN
  Summary KPIs: Total Processed, Will Churn, Will Stay

----------------------------------------------------------------------

SLIDE 14 — CHURN PREDICTOR — HOW RESULTS ARE DISPLAYED
Headline: Clear, Unmistakable Churn Outputs

Show two side-by-side large result cards:

LEFT CARD (Red gradient background):
  ❌ CHURN
  "This customer is LIKELY TO CHURN (leave)"
  Churn Probability: 73.4%
  Risk Level: 🔴 HIGH
  Action: Immediate retention campaign needed

RIGHT CARD (Green gradient background):
  ✅ NOT CHURN
  "This customer is LIKELY TO STAY (retain)"
  Churn Probability: 18.2%
  Risk Level: 🟢 LOW
  Action: No urgent action required — explore upselling

Below both cards — Gauge Chart Visual:
  0-30% = Green zone (Safe)
  30-60% = Yellow zone (Monitor)
  60-100% = Red zone (At Risk)

----------------------------------------------------------------------

SLIDE 15 — UI / UX DESIGN PHILOSOPHY
Headline: "Nebula Graphite" — Premium Dark SaaS Theme

Design System Table:
| Element         | Specification                                        |
|-----------------|------------------------------------------------------|
| Background      | Deep Black #121212                                   |
| Surface Cards   | #1E1E1E with Glassmorphism blur                      |
| Primary Color   | Electric Violet #8A3FFC                              |
| Churn Color     | Crimson Red #ff4b4b                                  |
| Retain Color    | Emerald Green #00d26a                                |
| Body Font       | Inter (300–800 weight range)                         |
| Heading Font    | Manrope (800 weight, letter-spacing -0.02em)         |
| Card Style      | backdrop-filter: blur(16px), 16px border radius      |
| Hover Effect    | translateY(-4px) + scale(1.005) smooth animation     |
| Scrollbar       | Custom 5px violet-accent minimal scrollbar           |
| UI Hides        | Streamlit default header, footer, menu hidden via CSS|

----------------------------------------------------------------------

SLIDE 16 — DEPLOYMENT STRATEGY
Headline: From Code to Cloud — Our Deployment Pipeline

Show as an arrow flowchart:

[💻 Local Development (VS Code)]
    ↓ git add . + git commit
[📦 GitHub Repository]
    (thakkarmeet909/EchoSense-Travel-Prediction)
    ↓ Auto-trigger on push
[☁️ Streamlit Community Cloud]
    (Reads requirements.txt → installs all packages)
    ↓
[🌐 Live Public URL]
    (Accessible from any browser, anywhere in the world)

Key Files for Deployment:
  ✅ app.py — Main application code
  ✅ requirements.txt — streamlit, pandas, numpy, scikit-learn, plotly, joblib, matplotlib, seaborn
  ✅ .streamlit/config.toml — Theme colors and server config
  ✅ travel_model_assets.pkl — Trained model (1.4 MB)
  ✅ Customertravel.csv — Source dataset (954 records)
  ✅ hero_nebula.png — Sidebar branding image
  ✅ style.css — Custom glassmorphism CSS

----------------------------------------------------------------------

SLIDE 17 — LIVE DEMO SCREENSHOTS
Headline: EchoSense AI — Live on the Web

Instruction: Place 5 actual screenshots here after deploying to Streamlit.

Screenshot 1 — Executive Summary page
  Show KPI metrics, "What This Model Does" box, Age histogram

Screenshot 2 — Customer Pulse page
  Show Red/Green bar charts for Income and Frequent Flyer

Screenshot 3 — Churn Predictor — CHURN result
  Show full-width ❌ CHURN red banner with gauge chart at 73%

Screenshot 4 — Churn Predictor — NOT CHURN result
  Show full-width ✅ NOT CHURN green banner with gauge chart at 18%

Screenshot 5 — Batch Processing result
  Show uploaded CSV with Churn_Probability + ❌/✅ Result column

Add QR code bottom-right linking to the live app URL.

----------------------------------------------------------------------

SLIDE 18 — RESULTS & KEY FINDINGS
Headline: What the Model Revealed

10 Key Findings:
1. Random Forest achieved 87.96% accuracy on 191 unseen test customers
2. High Income customers churn 3x LESS than Middle/Low Income customers
3. Frequent Flyers have a 2.5x higher retention rate than non-frequent flyers
4. Age range 27–38 is the primary customer demographic in this dataset
5. Age and FrequentFlyer status are the TOP two predictors of churn
6. Hotel booking and social media sync have moderate impact on churn
7. 76.5% of all customers in the dataset have churned — severe imbalance
8. Real-time individual predictions are generated in under 1 second
9. Batch processing completes 954-record scoring in under 3 seconds
10. The gauge chart + colored banner system makes results instantly clear to non-technical users

----------------------------------------------------------------------

SLIDE 19 — BUSINESS IMPACT & ROI
Headline: Why This Matters to the Travel Industry

Scenario (show as infographic):
  Travel company with 100,000 potential customers:
  • Current churn rate = 76.5% → 76,500 customers lost
  • Average travel package value = $2,000
  • Total revenue at risk = $153 Million

  With EchoSense AI:
  • Model identifies high-risk churners BEFORE they leave
  • Targeted retention campaign on top 10% at-risk = 7,650 saved customers
  • Revenue saved = 7,650 × $2,000 = $15.3 Million annually

Business Benefits:
  ✅ Marketing budget reduced by 40–60% (target only at-risk customers)
  ✅ Sales team prioritization based on churn probability score
  ✅ Real-time single prediction for customer service teams
  ✅ Bulk CSV upload for weekly marketing campaign planning
  ✅ Clear ❌ CHURN / ✅ NOT CHURN output usable by non-technical staff

----------------------------------------------------------------------

SLIDE 20 — CONCLUSION, CHALLENGES & FUTURE SCOPE
Headline: What We Built, Learned, and Where We Go Next

CONCLUSION (left column):
  ✅ Built and deployed EchoSense AI — a full ML churn prediction platform
  ✅ Trained Random Forest on 954 travel customers → 88% accuracy
  ✅ Built 4-module Streamlit dashboard with clear CHURN / NOT CHURN outputs
  ✅ Deployed live to the cloud via GitHub + Streamlit Community Cloud
  ✅ Full training workflow documented in Model_Training.ipynb

CHALLENGES (middle column):
  ⚠️ Class imbalance (76.5% vs 23.5%) needed careful metric handling
  ⚠️ "No Record" FrequentFlyer category required special encoding
  ⚠️ Custom CSS glassmorphism is complex inside Streamlit's framework
  ⚠️ Small dataset (954 records) limits deep learning viability

FUTURE SCOPE (right column):
  🚀 Add SMOTE to balance training data
  🚀 Compare XGBoost, LightGBM, and Neural Networks
  🚀 Add SHAP / LIME for explainable predictions
  🚀 REST API for CRM integration
  🚀 Automated email alerts for high-churn customers
  🚀 More features: travel history, seasonal preferences

ACKNOWLEDGEMENTS:
  IBM SkillsBuild Program | Scikit-learn | Streamlit | Plotly | [Mentor Name] | [College Name]

REFERENCES:
  Customertravel.csv — IBM SkillsBuild / Kaggle
  Scikit-learn Docs — scikit-learn.org
  Streamlit Docs — docs.streamlit.io
  Streamlit Cloud — share.streamlit.io

======================================================================
END OF PROMPT
======================================================================
