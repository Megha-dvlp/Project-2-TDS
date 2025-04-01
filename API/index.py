from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# Initialize FastAPI
app = FastAPI()

# Configure Gemini API Key
API_KEY = "AIzaSyB7iuEYqx8n7bAj6Vc2TDS9T_j9yr3cwhs"  # Replace with your actual key
genai.configure(api_key=API_KEY)

# Define request model
class QuestionRequest(BaseModel):
    question: str

# API Endpoint
@app.post("/api/")
async def answer_question(request: QuestionRequest):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # Use the correct model available for your API key
        response = model.generate_content(request.question)
        return {"answer": response.text}
    
    except Exception as e:
        return {"error": str(e)}
