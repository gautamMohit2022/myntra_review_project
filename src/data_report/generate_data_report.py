import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import os, sys
from src.exception import CustomException

# ✅ Wide layout for better fitting charts and content
st.set_page_config(layout="wide")

class DashboardGenerator:
    def __init__(self, data):
        # Convert to DataFrame if data is a list
        if isinstance(data, list):
            self.data = pd.DataFrame(data)
        else:
            self.data = data

    def display_general_info(self):
        st.header('📊 General Information')

        # Convert columns safely
        self.data['Over_All_Rating'] = pd.to_numeric(self.data['Over_All_Rating'], errors='coerce')
        self.data['Price'] = pd.to_numeric(
            self.data['Price'].apply(lambda x: x.replace("₹", "") if isinstance(x, str) else x),
            errors='coerce')
        self.data["Rating"] = pd.to_numeric(self.data['Rating'], errors='coerce')

        # Shorten product names for display
        def shorten(name, limit=50):
            return name if len(name) <= limit else name[:limit] + "..."

        # 📈 Pie Chart - Average Ratings by Product
        product_ratings = self.data.groupby('Product Name', as_index=False)['Over_All_Rating'].mean().dropna()
        product_ratings["Short Name"] = product_ratings["Product Name"].apply(shorten)

        with st.container():
            st.subheader("📈 Average Ratings by Product")
            fig_pie = px.pie(
                product_ratings,
                values='Over_All_Rating',
                names='Short Name',
                title='Average Ratings by Product',
                hover_data=['Product Name']
            )
            fig_pie.update_traces(textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)

        # 💸 Bar Chart - Average Prices
        avg_prices = self.data.groupby('Product Name', as_index=False)['Price'].mean().dropna()
        avg_prices["Short Name"] = avg_prices["Product Name"].apply(shorten)

        with st.container():
            st.subheader("💸 Average Price Comparison")
            fig_bar = px.bar(
                avg_prices,
                x='Short Name',
                y='Price',
                color='Short Name',
                title='Average Price Comparison Between Products',
                hover_data=['Product Name'],
                color_discrete_sequence=px.colors.qualitative.Bold
            )
            fig_bar.update_layout(
                xaxis_tickangle=-30,
                xaxis_title='Product',
                yaxis_title='Average Price'
            )
            st.plotly_chart(fig_bar, use_container_width=True)

    def display_product_sections(self):
        st.header('🧾 Product Sections')

        product_names = self.data['Product Name'].unique()
        cols_per_row = 2  # You can change to 3 if screen is wider

        for i in range(0, len(product_names), cols_per_row):
            row = st.columns(cols_per_row)

            for j in range(cols_per_row):
                if i + j < len(product_names):
                    product_name = product_names[i + j]
                    product_data = self.data[self.data['Product Name'] == product_name]

                    with row[j]:
                        st.subheader(f'📦 {product_name}')

                        # Display price
                        avg_price = product_data['Price'].mean()
                        st.markdown(f"💰 **Average Price:** ₹{avg_price:.2f}")

                        # Display rating
                        avg_rating = product_data['Over_All_Rating'].mean()
                        st.markdown(f"⭐ **Average Rating:** {avg_rating:.2f}")

                        # Positive reviews
                        positive_reviews = product_data[product_data['Rating'] >= 4.5].nlargest(5, 'Rating')
                        st.subheader('✅ Positive Reviews')
                        for _, row_data in positive_reviews.iterrows():
                            st.markdown(f"✨ Rating: {row_data['Rating']} - {row_data['Comment']}")

                        # Negative reviews
                        negative_reviews = product_data[product_data['Rating'] <= 2].nsmallest(5, 'Rating')
                        st.subheader('❌ Negative Reviews')
                        for _, row_data in negative_reviews.iterrows():
                            st.markdown(f"💢 Rating: {row_data['Rating']} - {row_data['Comment']}")

                        # Rating counts
                        st.subheader('📈 Rating Counts')
                        rating_counts = product_data['Rating'].value_counts().sort_index(ascending=False)
                        for rating, count in rating_counts.items():
                            st.write(f"🔹 Rating {rating} count: {count}")
