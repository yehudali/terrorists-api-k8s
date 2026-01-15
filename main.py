from fastapi import FastAPI

from db import MongoDBInteractor, TeroristCllas, get_5_most_dangerous_terrorist

from fastapi import UploadFile, Query, Form
import pandas as pd
import uvicorn
db = MongoDBInteractor()
app = FastAPI()
    

@app.get("/")
def hello():
    return{"message" : "Welcome to Fastapi server!" }

@app.post("/top-threats")
def foo(file: UploadFile):
    df = pd.read_csv(file.file)
    df_most_5_dangerous = get_5_most_dangerous_terrorist(df)
    print(df_most_5_dangerous)

    try:
        saved=db.save_most_5_dangerous(df_most_5_dangerous.to_dict())
        print(saved)
        if not saved:
            raise Exception("the: saved=db.save_most_5_dangerous(most_5_dangerous), not save ")
        return {"saved":df_most_5_dangerous.to_dict()}

    except Exception as e:
        print(f"eror:{e}")




# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)