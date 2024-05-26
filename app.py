from fastapi import FastAPI, Request, HTTPException
import uvicorn
import os
from fastapi.responses import RedirectResponse, Response
from textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response(content="Training successful")
    except Exception as e:
        return Response(content=f"Error occurred: {e}", status_code=500)

@app.post("/predict")
async def predict_route(text: str):
    try:
        obj = PredictionPipeline()
        result = obj.predict(text)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
