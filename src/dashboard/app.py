import streamlit as st
import pandas as pd
import sqlite3

# Connecting to SQLite database
conn = sqlite3.connect('../../data/mercadolivre.db')

# Loading data from 'mercadolivre_products table into a pandas dataframe
df = pd.read_sql_query('select * from mercadolivre_products', conn)

# Closing database connection
conn.close()

# Application title
st.title('Market Research - Sports Shoes on :blue[Mercado Livre]')

# Setting up the layout for KPI visualization
st.subheader('Main KPIs')
col1, col2, col3 = st.columns(3)

# KPI 1: Item Quantity Total
total_items = df.shape[0]
col1.metric(label='Item quantity total', value=total_items, border=True)

# KPI 2: Unique Brands Quantity
unique_brands = df['brand'].nunique()
col2.metric(label='Unique brands quantity', value=unique_brands, border=True)

# KPI 3: 'New Price' average in Brazillian Reais (BRL)
new_price_avg = df['new_price'].mean()
col3.metric(label='Current average products price', value=f'R${new_price_avg:.2f}', border=True)

# Most found brands up to the 10th page
st.subheader(':blue[Brand] - Most found up to the 10th page')
col1, col2 = st.columns([4, 2])
top_10_pages_brand = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brand)
col2.write(top_10_pages_brand)

# Average price by brand
st.subheader(':blue[Brand] - Average price')
col1, col2 = st.columns([4,2])
avg_brand_price = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(avg_brand_price)
col2.write(avg_brand_price)

# Customer satisfaction by brand
st.subheader(':blue[Brand] - Customer satisfaction')
col1, col2 = st.columns([4,2])
non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)