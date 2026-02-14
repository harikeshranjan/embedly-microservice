from sentence_transformers import SentenceTransformer
from .config import MODEL_NAME

# Load the model once at startup to avoid reloading it for every request
model = SentenceTransformer(MODEL_NAME)


def generate_embedding(text: str) -> list[float]:
    """
    Generate an embedding for the given text using the pre-loaded model.

    Args:
        text (str): The input text to be embedded.

    Returns:
        list[float]: The generated embedding as a list of floats.
    """
    return model.encode(text).tolist()
