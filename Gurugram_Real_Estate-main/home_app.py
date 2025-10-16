import streamlit as st

# Page config
st.set_page_config(
    page_title="Gurugram Real Estate Analytics",
    layout="wide"
)

# Main title
st.title("🏠 Gurugram Real Estate Analytics & Prediction")
st.write(
    """
    Welcome to the **Gurugram Real Estate Platform** 🚀  
    This website provides **data-driven insights, visual analytics, property recommendations, 
    and price predictions** for real estate in Gurugram.  
    Use the sidebar to navigate between the different apps.
    """
)

# Overview of features
st.header("🔎 What You Can Do Here")
st.markdown(
    """
    - 📊 **Analytics Dashboard** – Explore visual insights like price trends, sector comparisons, 
      word clouds, and property-type distributions.  
    - 🧭 **Find Apartments** – Search apartments within a chosen radius from any location 
      and get **AI-powered property recommendations**.  
    - 💰 **Price Prediction** – Enter property details to get an estimated **price range** 
      using a trained ML pipeline.  
    """
)

# Sections overview
st.header("📂 Pages in This App")
st.markdown(
    """
    - **Analytics** → Interactive plots, word clouds, and comparisons.  
    - **Recommend Apartments** → Location-based search + Similar property recommendations.  
    - **Price Prediction** → ML-based property price prediction.  
    """
)

# Footer / Call to action
st.info("👉 Use the left sidebar to navigate to different pages and start exploring!")
