# Embedly

## Overview

**Embedly** is a microservice built with FastAPI that demonstrates the principles of semantic search and cosine similarity on a small scale. This project serves as a practical example for developers and researchers interested in understanding and implementing semantic search techniques using modern machine learning embeddings.

## Features

- **Semantic Search:** Efficiently retrieves documents or items based on semantic meaning rather than keyword matching.
- **Cosine Similarity:** Utilizes cosine similarity to measure the closeness between vector embeddings, enabling accurate and relevant search results.
- **FastAPI Integration:** Leverages the speed and simplicity of FastAPI for building robust and scalable APIs.
- **Lightweight & Modular:** Designed for easy experimentation and extension, suitable for educational purposes and prototyping.

## Use Cases

- Building intelligent search engines for documents, FAQs, or product catalogs.
- Experimenting with embedding models and similarity metrics.
- Learning and teaching the fundamentals of semantic search in modern applications.

## Getting Started

1. **Clone the Repository:**
  ```bash
  git clone <repository-url>
  cd embedly
  ```

2. **Install Dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

3. **Run the Service:**
  ```bash
  uvicorn main:app --reload
  ```

4. **Access the API Documentation:**
  Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive API documentation powered by Swagger UI.

## API Endpoints

- `POST /search`: Submit a query and retrieve semantically similar items.
- `POST /add`: Add new items/documents to the search index.

## Technologies Used

- **FastAPI:** High-performance web framework for building APIs.
- **NumPy:** Efficient numerical computations for vector operations.
- **Pre-trained Embedding Models:** For generating semantic representations of text.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Inspired by advancements in natural language processing and semantic search.
- Built with ❤️ using FastAPI and open-source tools.