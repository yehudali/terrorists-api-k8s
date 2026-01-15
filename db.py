import os
import pandas as ps
from dotenv import load_dotenv
from pandas import DataFrame
from models import TeroristCllas
from pymongo import MongoClient


class MongoDBConnector:
    def __init__(self) -> None:
        self.mongo_host =os.getenv("MONGO_HOST", "mongo-0.mongo")
        self.mongo_port = int(os.getenv("MONGO_PORT", 27017))
        self.username = os.getenv("MONGO_USERNAME", "admin")
        self.db_name = os.getenv("MONGO_DB","threat_db")
        self.mongo_auth_source = os.getenv("MONGO_AUTH_SOURCE","admin" )

        uri = f'mongodb://{self.mongo_host}:{int(self.mongo_port)}/'
    
        self.client = MongoClient(uri)
        self.db = self.client[self.username]
        self.collection = self.db[self.db_name]


class MongoDBInteractor:
    def __init__(self) -> None:
        self.db_connector =  MongoDBConnector()

    def save_most_5_dangerous(self,dangeres:dict) -> bool:
        print(self.db_connector.collection)
        try:
            x = self.db_connector.collection.insert_many([dangeres])
            print(f"saved?:{x}")
            return True
        except Exception as e:
            print(f"eror{e}")
            return False

def get_5_most_dangerous_terrorist(df:DataFrame)->DataFrame:
    df =  df.loc[:, ['name', 'location', 'danger_rate']]
    df = df.sort_values("danger_rate",ascending=False)
    df=df.loc[:4]
    return df



# def df_to_teroristCllas_respons(df:DataFrame)-> list[TeroristCllas]:
#     all_clases=[]
#     for _, row in df.iterrows():
#         try:

#             all_clases.append(TeroristCllas(name= row.get(""),location="", danger_rate="").model_dump())
#         except:
#             print("I skipped a line in the dataframe")

#     return all_clases


