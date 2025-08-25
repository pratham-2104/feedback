from fastapi import FastAPI, Request
from textblob import TextBlob
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Sentiment Analysis API! Use /analyze to test feedback."}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify ["http://127.0.0.1:5500"] if running frontend on Live Server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    feedback = data.get("feedback", "")
    analysis = TextBlob(feedback)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😀"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return {"feedback": feedback, "sentiment": sentiment, "polarity": polarity}
