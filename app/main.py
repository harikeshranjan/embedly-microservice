from fastapi import FastAPI, HTTPException
from .schemas import EmbedRequest, EmbedResponse
from .model import generate_embedding
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="Embedly API",
    description="A simple API to generate text embeddings using a pre-trained model.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:3000")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Health Check"])
def health_check():
    """
    Health check endpoint to verify that the API is running.
    """
    return {"status": "ok"}


@app.post("/embed", response_model=EmbedResponse, tags=["Embedding"])
def embed(request: EmbedRequest):
    """
    Generate an embedding for the given text.

    Args:
        request (EmbedRequest): The request body containing the text to be embedded.
    Returns:
        EmbedResponse: The response containing the generated embedding.

    Raises:
        HTTPException: If the input text is empty or if there is an error during embedding generation.
    """
    try:
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Input text cannot be empty.")

        embedding = generate_embedding(request.text)

        return {"embedding": embedding}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
