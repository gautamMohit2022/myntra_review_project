import pandas as pd
import streamlit as st
from src.cloud_io import MongoIO
from src.constants import SESSION_PRODUCT_KEY
from src.scrapper.scrape import ScrapeReviews

st.set_page_config(
    "myntra-review-scrapper"
)
st.title("Myntra Review Scrapper")
st.session_state["date"] = False

def form_input():
    product = st.text_input("Search Products")
    st.session_state[SESSION_PRODUCT_KEY] = product
    no_of_products = st.number_input("No of products to search",
                                     step=1,
                                     min_value=1)
    if st.button("Scrape Reviews"):
        scrapper = ScrapeReviews(
            product_name=product,
            no_of_products=int(no_of_products)
        )
        try:
            scrapped_data = scrapper.get_review_data()
            if scrapped_data is not None:
                st.session_state["data"] = True
                mongoio = MongoIO()
                mongoio.store_reviews(product_name=product,
                                      reviews=scrapped_data)
                print("Stored data into Mongodb")
            st.dataframe(scrapped_data)
        except Exception as e:
            st.error(f"Scraping failed: {e}")

form_input()
