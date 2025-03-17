from read_data import read_data
import duckdb
import streamlit as st

def approved_by_area_bar():
    # Load the dataset
    df = read_data()
    # Use DuckDB to query and aggregate the data
    df = duckdb.query("""
                      SELECT utbildningsområde, COUNT(*) AS Beviljade
                      FROM df
                      WHERE beslut = 'Beviljad'
                      GROUP BY utbildningsområde
                      ORDER BY Beviljade
                      DESC
                      """).df()
    # Display the chart 
    st.bar_chart(df, x = "Utbildningsområde", y = "Beviljade")