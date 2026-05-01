---
title: EchoSense AI
emoji: 🧬
colorFrom: blue
colorTo: indigo
sdk: streamlit
app_file: app.py
pinned: false
---

# 🧬 EchoSense AI: Predictive Travel Intelligence

![EchoSense Banner](hero_new.png)

## 🚀 Overview
EchoSense AI is a premium, enterprise-grade customer travel package purchase prediction platform. By leveraging Random Forest architectures and behavioral analytics, EchoSense provides real-time purchase probability assessments for travel industry customers.

This project was built to transform raw customer data into actionable business intelligence for the travel and tourism industry.

## ✨ Key Features
- **Predictive Engine**: Real-time purchase probability calculation with 88% accuracy.
- **Customer Pulse**: Interactive EDA modules for deep-dive behavioral analysis.
- **Batch Processing**: Collective prediction for entire customer registries via CSV upload.
- **Cyberpunk Midnight UI**: A state-of-the-art, glassmorphism-based dashboard experience.

## 📊 Dataset
- **Source**: Customertravel.csv
- **Records**: 954 customers
- **Features**: Age, FrequentFlyer, AnnualIncomeClass, ServicesOpted, AccountSyncedToSocialMedia, BookedHotelOrNot
- **Target**: Binary (0 = Not Purchased, 1 = Purchased)

## 🛠️ Technology Stack
- **Dashboard**: [Streamlit](https://streamlit.io/)
- **Intelligence Engine**: [Scikit-learn](https://scikit-learn.org/) (Random Forest)
- **Data Engineering**: [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
- **Visual Intelligence**: [Plotly](https://plotly.com/python/), [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **Theming**: Custom Vanilla CSS with Glassmorphism

## 📦 Local Setup
1. Clone the repository:
   ```bash
   git clone <repo-link>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Train the model (run `Model_Training.ipynb` notebook)
4. Boot the engine:
   ```bash
   streamlit run app.py
   ```

## 🌐 Deployment
Optimized for **Hugging Face Spaces** with Streamlit SDK.

---
*Developed for IBM SkillsBuild Final Project*  
*EchoSense AI | Travel Intelligence Lab*
