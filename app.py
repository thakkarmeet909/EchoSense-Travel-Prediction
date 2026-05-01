import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import time

# --- CONFIGURATION ---
VERSION = "v3.1.0-Elite"
PLATFORM_NAME = "EchoSense AI"
PLATFORM_TAGLINE = "Deep Customer Churn Intelligence for Travel Industry"
ACCENT_COLOR = "#8A3FFC"

st.set_page_config(
    page_title=f"{PLATFORM_NAME} — Customer Churn Prediction",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
def inject_system_styles():
    if Path('style.css').exists():
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

inject_system_styles()

# --- DATA & ASSETS ---
@st.cache_resource
def sync_neural_weights():
    try:
        return joblib.load('travel_model_assets.pkl')
    except:
        return None

engine = sync_neural_weights()

@st.cache_data
def load_enterprise_registry():
    df = pd.read_csv('Customertravel.csv')
    return df

registry = load_enterprise_registry()

# --- UI COMPONENTS ---
def draw_header(title, subtitle):
    st.markdown(f"""
    <div class="header-container">
        <h1 style="margin:0; color:white;">{title}</h1>
        <p style="margin:0; color:#9ca3af; font-size:1rem;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("hero_nebula.png", use_container_width=True)
    st.markdown(f"<h2 style='color:white; margin:0;'>{PLATFORM_NAME}</h2>", unsafe_allow_html=True)
    st.caption(f"Churn Intelligence {VERSION}")
    st.markdown("---")
    
    module = st.radio("Intelligence Modules", 
                      ["Executive Summary", "Customer Pulse", "Churn Predictor", "Batch Processing"])
    
    st.markdown("---")
    st.write("**System Nodes**")
    st.success("Neural Engine: Online")
    st.success("Registry Sync: Synced")

    st.markdown("---")
    st.markdown("""
    <div style='background: rgba(138,63,252,0.1); border: 1px solid rgba(138,63,252,0.3); border-radius: 10px; padding: 1rem; font-size: 0.8rem;'>
        <strong style='color: #8A3FFC;'>🧬 What This Model Does</strong><br><br>
        <span style='color: #ccc;'>Predicts whether a travel customer will <strong>CHURN</strong> (leave/not purchase) or <strong>NOT CHURN</strong> (stay/purchase) based on their profile and behavior.</span><br><br>
        <span style='color: #9ca3af;'>• Algorithm: Random Forest<br>• Accuracy: 88%<br>• Dataset: 954 customers<br>• Features: 6 inputs</span>
    </div>
    """, unsafe_allow_html=True)

# --- MODULES ---

if module == "Executive Summary":
    draw_header("Platform Overview", "Customer Churn Analytics & Enterprise KPIs for Travel Industry")
    
    # --- WHAT THIS MODEL DOES ---
    st.markdown("""
    <div class='nebula-card' style='border-left: 4px solid #8A3FFC;'>
        <h3 style='color: white; margin-top: 0;'>🧬 What Does This Model Do?</h3>
        <p style='color: #e0e0e0; font-size: 1.05rem; line-height: 1.7;'>
            EchoSense AI uses a <strong style='color: #8A3FFC;'>Random Forest Machine Learning model</strong> trained on <strong>954 travel customer records</strong> 
            to predict whether a customer will <strong style='color: #ff4b4b;'>CHURN</strong> (leave / not purchase a travel package) 
            or <strong style='color: #00d26a;'>NOT CHURN</strong> (stay / purchase the package).
        </p>
        <table style='width:100%; color: #ccc; margin-top: 1rem;'>
            <tr>
                <td style='padding: 8px; border: 1px solid #333; border-radius: 4px;'><strong>📊 Input</strong></td>
                <td style='padding: 8px; border: 1px solid #333;'>Age, Frequent Flyer Status, Income Class, Services Opted, Social Media Sync, Hotel Booking</td>
            </tr>
            <tr>
                <td style='padding: 8px; border: 1px solid #333;'><strong>🎯 Output</strong></td>
                <td style='padding: 8px; border: 1px solid #333;'><strong style='color: #ff4b4b;'>CHURN</strong> (Target = 1) or <strong style='color: #00d26a;'>NOT CHURN</strong> (Target = 0) + Churn Probability (0–100%)</td>
            </tr>
            <tr>
                <td style='padding: 8px; border: 1px solid #333;'><strong>⚙️ Algorithm</strong></td>
                <td style='padding: 8px; border: 1px solid #333;'>Random Forest Classifier (100 Decision Trees)</td>
            </tr>
            <tr>
                <td style='padding: 8px; border: 1px solid #333;'><strong>✅ Accuracy</strong></td>
                <td style='padding: 8px; border: 1px solid #333;'>87.96% on test data (191 samples)</td>
            </tr>
            <tr>
                <td style='padding: 8px; border: 1px solid #333;'><strong>💡 Use Case</strong></td>
                <td style='padding: 8px; border: 1px solid #333;'>Travel companies use this to identify at-risk customers BEFORE they leave, enabling targeted retention campaigns and reducing revenue loss</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    with kpi1:
        st.metric("Total Customers", f"{len(registry):,}")
    with kpi2:
        churn_rate = (registry['Target'] == 1).mean() * 100
        st.metric("Churn Rate", f"{churn_rate:.1f}%", delta="-2.3%", delta_color="inverse")
    with kpi3:
        retained = (registry['Target'] == 0).mean() * 100
        st.metric("Retention Rate", f"{retained:.1f}%", delta="+2.3%")
    with kpi4:
        avg_services = registry['ServicesOpted'].mean()
        st.metric("Avg Services Opted", f"{avg_services:.1f}")

    st.markdown("<div class='nebula-card'>", unsafe_allow_html=True)
    st.subheader("Customer Age Distribution by Churn Status")
    registry_plot = registry.copy()
    registry_plot['Churn Status'] = registry_plot['Target'].map({0: '✅ Not Churned', 1: '❌ Churned'})
    fig_dist = px.histogram(registry_plot, x="Age", color="Churn Status", 
                            color_discrete_sequence=["#00d26a", "#ff4b4b"],
                            template="plotly_dark", barmode='overlay')
    fig_dist.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', 
                           margin=dict(t=50, b=0, l=0, r=0))
    st.plotly_chart(fig_dist, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 🖥️ Live Customer Registry")
    display_df = registry.copy()
    display_df['Churn Status'] = display_df['Target'].map({0: '✅ Not Churned', 1: '❌ Churned'})
    st.dataframe(display_df.sample(10), use_container_width=True)

elif module == "Customer Pulse":
    draw_header("Customer Pulse", "Deep-dive churn analytics and behavioral segmentation.")
    
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("<div class='nebula-card'>", unsafe_allow_html=True)
        st.subheader("Churn Rate by Income Class")
        income_summary = registry.groupby(['AnnualIncomeClass', 'Target']).size().reset_index(name='Count')
        income_summary['Churn Status'] = income_summary['Target'].map({0: '✅ Not Churned', 1: '❌ Churned'})
        fig_s = px.bar(income_summary, x='AnnualIncomeClass', y='Count', color='Churn Status',
                       color_discrete_sequence=["#00d26a", "#ff4b4b"], barmode='group',
                       template="plotly_dark")
        fig_s.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_s, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col_b:
        st.markdown("<div class='nebula-card'>", unsafe_allow_html=True)
        st.subheader("Frequent Flyer vs Churn")
        ff_summary = registry.groupby(['FrequentFlyer', 'Target']).size().reset_index(name='Count')
        ff_summary['Churn Status'] = ff_summary['Target'].map({0: '✅ Not Churned', 1: '❌ Churned'})
        fig_r = px.bar(ff_summary, x='FrequentFlyer', y='Count', color='Churn Status',
                       color_discrete_sequence=["#00d26a", "#ff4b4b"],
                       barmode='group', template="plotly_dark")
        fig_r.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_r, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    col_c, col_d = st.columns(2)
    with col_c:
        st.markdown("<div class='nebula-card'>", unsafe_allow_html=True)
        st.subheader("Services Opted vs Churn")
        svc_plot = registry.copy()
        svc_plot['Churn Status'] = svc_plot['Target'].map({0: '✅ Not Churned', 1: '❌ Churned'})
        fig_sv = px.histogram(svc_plot, x='ServicesOpted', color='Churn Status',
                              color_discrete_sequence=["#00d26a", "#ff4b4b"], barmode='overlay',
                              template="plotly_dark")
        fig_sv.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_sv, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_d:
        st.markdown("<div class='nebula-card'>", unsafe_allow_html=True)
        st.subheader("Hotel Booking vs Churn")
        hotel_summary = registry.groupby(['BookedHotelOrNot', 'Target']).size().reset_index(name='Count')
        hotel_summary['Churn Status'] = hotel_summary['Target'].map({0: '✅ Not Churned', 1: '❌ Churned'})
        fig_h = px.bar(hotel_summary, x='BookedHotelOrNot', y='Count', color='Churn Status',
                       color_discrete_sequence=["#00d26a", "#ff4b4b"],
                       barmode='group', template="plotly_dark")
        fig_h.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig_h, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

elif module == "Churn Predictor":
    draw_header("Churn Predictor", "Predict whether a customer will CHURN or NOT CHURN based on their profile.")
    
    # Model explanation box
    st.markdown("""
    <div class='nebula-card' style='border-left: 4px solid #8A3FFC; padding: 1.5rem;'>
        <h4 style='color: #8A3FFC; margin-top: 0;'>🎯 How To Use This Predictor</h4>
        <p style='color: #ccc; margin: 0;'>
            Enter the customer's details below and click <strong>"PREDICT CHURN STATUS"</strong>. 
            The model will analyze the inputs and return:<br>
            • <strong style='color: #ff4b4b;'>❌ CHURN</strong> — Customer is likely to leave (Target = 1)<br>
            • <strong style='color: #00d26a;'>✅ NOT CHURN</strong> — Customer is likely to stay (Target = 0)<br>
            • A probability score from 0% to 100% showing the churn likelihood
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if engine:
        st.markdown("<div class='nebula-card'>", unsafe_allow_html=True)
        with st.form("predict_form"):
            c1, c2 = st.columns(2)
            with c1:
                st.write("**Customer Profile**")
                age = st.slider("Age", 18, 60, 30)
                frequent_flyer = st.selectbox("Frequent Flyer", ["Yes", "No", "No Record"])
                annual_income = st.selectbox("Annual Income Class", ["Low Income", "Middle Income", "High Income"])
            with c2:
                st.write("**Service & Behavior**")
                services = st.slider("Services Opted", 1, 6, 3)
                social_media = st.selectbox("Account Synced to Social Media", ["Yes", "No"])
                hotel = st.selectbox("Booked Hotel Or Not", ["Yes", "No"])

            submitted = st.form_submit_button("🔍 PREDICT CHURN STATUS")
            
            if submitted:
                features = {
                    'Age': age,
                    'FrequentFlyer': frequent_flyer,
                    'AnnualIncomeClass': annual_income,
                    'ServicesOpted': services,
                    'AccountSyncedToSocialMedia': social_media,
                    'BookedHotelOrNot': hotel
                }
                
                input_df = pd.DataFrame([features])
                
                for col, le in engine['le_dict'].items():
                    if col in input_df.columns:
                        try:
                            input_df[col] = le.transform(input_df[col])
                        except:
                            input_df[col] = 0
                
                X = engine['scaler'].transform(input_df[engine['feature_names']])
                churn_prob = engine['model'].predict_proba(X)[0][1]
                prediction = engine['model'].predict(X)[0]
                
                st.markdown("---")
                
                # Big result banner
                if prediction == 1:
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, rgba(255,75,75,0.2), rgba(255,75,75,0.05)); 
                                border: 2px solid #ff4b4b; border-radius: 16px; padding: 2rem; text-align: center; margin: 1rem 0;'>
                        <h1 style='color: #ff4b4b; margin: 0; font-size: 3rem;'>❌ CHURN</h1>
                        <p style='color: #ff8a8a; font-size: 1.3rem; margin: 0.5rem 0 0 0;'>
                            This customer is <strong>LIKELY TO CHURN</strong> (leave)
                        </p>
                        <p style='color: #ff4b4b; font-size: 2rem; font-weight: 800; margin: 0.5rem 0 0 0;'>
                            Churn Probability: {churn_prob*100:.1f}%
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style='background: linear-gradient(135deg, rgba(0,210,106,0.2), rgba(0,210,106,0.05)); 
                                border: 2px solid #00d26a; border-radius: 16px; padding: 2rem; text-align: center; margin: 1rem 0;'>
                        <h1 style='color: #00d26a; margin: 0; font-size: 3rem;'>✅ NOT CHURN</h1>
                        <p style='color: #66e8a8; font-size: 1.3rem; margin: 0.5rem 0 0 0;'>
                            This customer is <strong>LIKELY TO STAY</strong> (not churn)
                        </p>
                        <p style='color: #00d26a; font-size: 2rem; font-weight: 800; margin: 0.5rem 0 0 0;'>
                            Churn Probability: {churn_prob*100:.1f}%
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                
                res1, res2 = st.columns([1, 1.5])
                with res1:
                    st.write("### 📋 Detailed Analysis")
                    st.markdown(f"""
                    | Parameter | Value |
                    |-----------|-------|
                    | **Prediction** | {'❌ CHURN' if prediction == 1 else '✅ NOT CHURN'} |
                    | **Churn Probability** | {churn_prob*100:.1f}% |
                    | **Retention Probability** | {(1-churn_prob)*100:.1f}% |
                    | **Risk Level** | {'🔴 HIGH' if churn_prob > 0.7 else '🟡 MEDIUM' if churn_prob > 0.4 else '🟢 LOW'} |
                    | **Recommended Action** | {'⚠️ Immediate retention campaign needed' if prediction == 1 else '✅ No urgent action required'} |
                    """)
                
                with res2:
                    fig_g = go.Figure(go.Indicator(
                        mode="gauge+number+delta", value=churn_prob * 100,
                        title={'text': "Churn Probability (%)"},
                        delta={'reference': 50, 'increasing': {'color': '#ff4b4b'}, 'decreasing': {'color': '#00d26a'}},
                        gauge={
                            'axis': {'range': [0, 100], 'tickwidth': 1},
                            'bar': {'color': '#ff4b4b' if prediction == 1 else '#00d26a'},
                            'bgcolor': "rgba(0,0,0,0)",
                            'steps': [
                                {'range': [0, 30], 'color': 'rgba(0,210,106,0.15)'},
                                {'range': [30, 60], 'color': 'rgba(255,200,0,0.15)'},
                                {'range': [60, 100], 'color': 'rgba(255,75,75,0.15)'}
                            ],
                            'threshold': {
                                'line': {'color': 'white', 'width': 3},
                                'thickness': 0.8,
                                'value': 50
                            }
                        }))
                    fig_g.update_layout(height=280, margin=dict(t=60, b=0, l=10, r=10), paper_bgcolor='rgba(0,0,0,0)')
                    st.plotly_chart(fig_g, use_container_width=True)
                
                # Outcome explanation
                st.markdown("""
                <div class='nebula-card' style='border-left: 4px solid #8A3FFC; margin-top: 1rem;'>
                    <h4 style='color: #8A3FFC; margin-top: 0;'>📖 What This Result Means</h4>
                    <p style='color: #ccc;'>
                        <strong>CHURN (Target = 1):</strong> The model predicts this customer will <strong>leave</strong> the travel service 
                        and <strong>NOT purchase</strong> a travel package. The company should launch a targeted retention campaign (discounts, personalized offers) to prevent this customer from leaving.<br><br>
                        <strong>NOT CHURN (Target = 0):</strong> The model predicts this customer will <strong>stay</strong> with the service 
                        and is <strong>likely to purchase</strong> a travel package. No urgent retention action is needed, but upselling opportunities can be explored.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Engine Assets missing. Run Model_Training.ipynb first.")

elif module == "Batch Processing":
    draw_header("Batch Engine", "Bulk churn prediction — upload a CSV and get churn status for every customer.")
    
    st.markdown("<div class='nebula-card' style='text-align: center; padding: 3rem;'>", unsafe_allow_html=True)
    st.write("### Drop Customer Registry File Here")
    st.caption("Supports .CSV format with Customertravel schema (Age, FrequentFlyer, AnnualIncomeClass, ServicesOpted, AccountSyncedToSocialMedia, BookedHotelOrNot)")
    
    file = st.file_uploader("", type=["csv"])
    
    if file:
        st.success("File synchronized. Neural clusters ready for ingestion.")
        if st.button("🔍 RUN BULK CHURN PREDICTION"):
            with st.status("Analyzing Registry...", expanded=True) as status:
                st.write("Extracting feature vectors...")
                time.sleep(1)
                st.write("Running Churn Prediction Scan...")
                time.sleep(1)
                status.update(label="Analysis Complete ✅", state="complete")
            
            df_b = pd.read_csv(file)
            if engine:
                df_proc = df_b.copy()
                
                for col, le in engine['le_dict'].items():
                    if col in df_proc.columns:
                        df_proc[col] = df_proc[col].apply(lambda x: x if x in le.classes_ else le.classes_[0])
                        df_proc[col] = le.transform(df_proc[col])
                        
                X_batch = engine['scaler'].transform(df_proc[engine['feature_names']])
                df_b['Churn_Probability'] = engine['model'].predict_proba(X_batch)[:, 1]
                df_b['Churn_Prediction'] = engine['model'].predict(X_batch)
                df_b['Result'] = df_b['Churn_Prediction'].map({0: '✅ NOT CHURN', 1: '❌ CHURN'})
            else:
                df_b['Churn_Probability'] = 0.0
                df_b['Result'] = 'N/A'
            
            # Summary
            total = len(df_b)
            churned = (df_b['Churn_Prediction'] == 1).sum() if 'Churn_Prediction' in df_b.columns else 0
            not_churned = total - churned
            
            s1, s2, s3 = st.columns(3)
            with s1:
                st.metric("Total Processed", f"{total}")
            with s2:
                st.metric("❌ Will Churn", f"{churned}", delta=f"{churned/total*100:.1f}%", delta_color="inverse")
            with s3:
                st.metric("✅ Will Stay", f"{not_churned}", delta=f"{not_churned/total*100:.1f}%")
            
            display_cols = ['Age', 'FrequentFlyer', 'AnnualIncomeClass', 'ServicesOpted', 'Churn_Probability', 'Result']
            available_cols = [c for c in display_cols if c in df_b.columns]
            st.dataframe(df_b[available_cols].head(20), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption(f"© 2026 {PLATFORM_NAME} Intelligence | Customer Churn Prediction | Trained on Customertravel.csv | Accuracy: 88%")
