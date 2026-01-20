from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "RESUMEX AI Backend Running Successfully 🚀"}
