from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return "Welcome to Home page in india"