"""
Abstraction layers for transacting with document collections.

Connection to cloud.mongodb.com.

Create environment variables:
  - MONGO_LOGIN
  - MONGO_PASSWORD
"""

import os

from pymongo import MongoClient


class Collection:

    def __init__(self, db_name: str = 'sample_airbnb',
                 collection_name: str = 'listingsAndReviews'):

        self.db_name = db_name
        self.collection_name = collection_name
        login = os.environ['MONGO_LOGIN']
        password = os.environ['MONGO_PASSWORD']
        conn_str = f"mongodb+srv://{login}:{password}" \
                   f"@cluster0.xnofp.mongodb.net/" \
                   f"myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(conn_str)
        cursor = client.get_database(self.db_name)
        self.collection = cursor[collection_name]

    def query(self, request: dict):
        """
        Process requests to the document base.
        Man: https://docs.mongodb.com/manual/tutorial/query-documents/
        """
        response = self.collection.find(request)
        for i in response:
            print(i)


if __name__ == '__main__':
    collection = Collection()
    collection.query(
        {"images.picture_url": {"$size": 20}}
    )
