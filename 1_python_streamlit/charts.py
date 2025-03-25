from read_data import read_data
# Import duckdb for SQL-like queries on DataFrames
import duckdb
# Import streamlit for interactive visualization
import streamlit as st

# A function to create a bar chart showing approvals by education area
def approved_by_area_bar():
    # Load the dataset
    df = read_data()
    
    # Use DuckDB to run an SQL query against the pandas DataFrame
    df= duckdb.query("""
                     SELECT utbildningsområde, COUNT(*) SD Beviljade
                     FROM df
                     WHERE beslut == 'Beviljad'
                     GROUP BY utbildningsområde
                     ORDER BY Beviljade
                     DESC
                     """).df()
    
    st.bar_chart(df, x = "Utibldningsområde", y = "Beviljade")
    
# - Plotting methods - 
#matplotlib plot
#plotly express plots