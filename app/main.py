from typing import Optional

from fastapi import FastAPI
import uvicorn

app = FastAPI()

print("Hellooo Worldd!!")

@app.get("/")
def read_root():
   return("Hellooo Worldd!!")
   
if __name__ == '__main__':
   uvicorn.run(app, port=8000, host="0.0.0.0")
