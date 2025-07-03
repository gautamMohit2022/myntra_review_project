from src.cloud_io import MongoIO
import pandas as pd

mongo = MongoIO()

df = pd.DataFrame([
    {"review": "Excellent product", "rating": 5},
    {"review": "Could be better", "rating": 3}
])

mongo.store_reviews("Test Product", df)

data = mongo.get_reviews("Test Product")
print(" Retrieved Reviews from MongoDB:\n", data)
