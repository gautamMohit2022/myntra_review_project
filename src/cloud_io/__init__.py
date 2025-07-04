import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import pandas as pd
from pymongo import MongoClient
from src.constants import *
from src.exception import CustomException

class MongoIO:
    mongo_ins = None

    def __init__(self):
        if MongoIO.mongo_ins is None:
            mongo_db_url = MONGODB_URL_KEY  # Make sure this contains the actual URI
            try:
                client = MongoClient(mongo_db_url)
                database = client[MONGO_DATABASE_NAME]
                MongoIO.mongo_ins = database
                print("Connected to MongoDB successfully!")

            except Exception as e:
                raise CustomException(e, sys)

        self.mongo_ins = MongoIO.mongo_ins

    def store_reviews(self, product_name: str, reviews: pd.DataFrame):
        try:
            collection_name = product_name.replace(" ", "_").lower()
            data_dict = reviews.to_dict(orient="records")
            self.mongo_ins[collection_name].insert_many(data_dict)

        except Exception as e:
            raise CustomException(e, sys)

    def get_reviews(self, product_name: str):
        try:
            collection_name = product_name.replace(" ", "_").lower()
            data = list(self.mongo_ins[collection_name].find({}, {"_id": 0}))
            return data

        except Exception as e:
            raise CustomException(e, sys)
