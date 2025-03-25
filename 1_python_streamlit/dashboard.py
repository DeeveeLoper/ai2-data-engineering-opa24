import streamlit as st
import plotly_express as px
import matplotlib.pyplot as plt
from kpis import approved_percentage, number_approved, total_applications, approved, provider_kpis
from read_data import read_data
from charts import approved_by_area_bar

df = read_data()

def layout():
    
    # Main title
    st.markdown("# YH dashboard 2024 application")
    # Dashborad description
    st.markdown("This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard.")
    
    # --- KPI section ---
    st.markdown("## KPIs in Sweden")
    labels = ("total_applications", "number approved", "approved percentage")
    # Create 3 columns
    cols = st.columns(3)
    kpis = (total_applications, number_approved, approved_percentage)
    
    # Display each KPI in its own column
    for col, label, kpi in zip(cols, labels, kpis):
        with col:
            st.metric(label=label, value=kpi)
    
    # Area analysis section
    st.markdown("## Aproved by area")
    approved_by_area_bar()
    
    # Provider specific analysis section
    st.markdown("## Simple statistics on a given provide")
    st.markdown("Search for an educational provider")

    # Dropdown to select an education provider
    provider = st.selectbox("Choose educational provider", 
                           df["Utbildningsanordnare administrativ enhet"].unique())
    
    # Get the specific KPIs for the selected provider
    provider_applications, provider_approved = provider_kpis(provider)
    # Display provider statistics
    st.markdown(f"This education provider {provider} has applied for {provider_applications} educations and gotten {provider_approved} educations approved")
    
    # Raw data section
    st.markdown("## Raw data")
    st.dataframe(df)


# Run the layout function when the script is executed directly
if __name__ == "__main__":
    layout()