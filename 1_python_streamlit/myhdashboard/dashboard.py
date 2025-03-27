import streamlit as st
from read_data import read_data
from kpis import approved_precentage, number_approved, total_applications, provider_kpis
from charts import approved_by_area_bar

# --- reading data --
df = read_data()

# --- Dashboard components --
#title
st.markdown("## YH Dashboard 2024 application")

st.markdown("This is a simple dashboard about higher vocational education in Sweden (yrkeshögskola). The results from the education can be filtered in this dashboard.")

#kpi components for all schools (horizontal layout)
st.markdown("## KPIs in Sweden")

labels = ("Total Applications", "Number of approved", "Approved precentage")
kpis = (total_applications, number_approved, approved_precentage)
cols = st.columns(3)

for col, label, kpi in zip(cols, labels, kpis):
    with col:
        st.metric(label, value=kpi)

# Chart components for areas
st.markdown("## Approved by area")
approved_by_area_bar()

# kpi components for one school
st.markdown ("## Simple statstistic on a given provier: ")

# Can add sort the providers alphabetically before displaying them in the selectbox
provider = st.selectbox("Choose one educational provider", df["Utbildningsanordnare administrativ enhet"].unique())

provider_applications, provider_approved = provider_kpis(provider)
st.markdown(f"This education providert {provider} has applied for {provider_applications} education and gotten {provider_approved} educations approved")

#data table
st.markdown("## Raw Data")
st.dataframe(df)