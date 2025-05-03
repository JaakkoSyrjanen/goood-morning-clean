from fastapi import FastAPI
from routes import auth  # <-- Import our new router

app = FastAPI()

app.include_router(auth.router)  # <-- Register it

@app.get("/")
def root():
    return {"message": "This is a working FastAPI app"}
