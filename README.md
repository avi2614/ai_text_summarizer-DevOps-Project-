# AI Text Summarizer - DevOps Project

## Overview

This project is an AI-powered text summarization tool built using Python and Hugging Face Transformers, designed to take large blocks of text and generate concise summaries. The tool is packaged as a Flask web application and is containerized using Docker, with DevOps automation via Jenkins for CI/CD.

## Features

- **Text Summarization:** Uses state-of-the-art transformer models (`sshleifer/distilbart-cnn-12-6`) to summarize input text.
- **Web Interface:** Simple web form for users to paste text and receive an instant summary.
- **Automated Testing:** Includes Pytest-based tests for model functionality.
- **Dockerized:** Easily build and run the application in a Docker container.
- **CI/CD Pipeline:** Jenkins pipeline automates build, test, and deployment steps, including pushing Docker images to Docker Hub.

## Getting Started

### Prerequisites

- Docker
- Python 3.9+
- (Optional) Jenkins for CI/CD

### Setup & Usage

#### 1. Clone the repository

```bash
git clone https://github.com/avi2614/ai_text_summarizer-DevOps-Project-.git
cd ai_text_summarizer-DevOps-Project-
```

#### 2. Build and Run with Docker

```bash
docker build -t flask-summarizer .
docker run -d --name summarizer -p 5000:5000 flask-summarizer
```

The app will be available at `http://localhost:5000`.

#### 3. Local Development

Install dependencies (if requirements.txt is present):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

#### 4. Running Tests

```bash
pytest
```

## DevOps Pipeline (Jenkins)

The provided `Jenkinsfile` will:

- Clone the repository.
- Build the Docker image.
- Run automated tests using Pytest.
- Push the image to Docker Hub (on main branch).
- Deploy the container.

You must set up Docker Hub credentials in Jenkins and update the `DOCKERHUB_USER` environment variable accordingly.

## File Structure

- `app.py` - Main Flask application
- `templates/index.html` - Web UI template
- `Dockerfile` - Docker build instructions
- `Jenkinsfile` - CI/CD pipeline definition
- `tests/` - Unit tests

## License

This project is for educational and demonstration purposes.

## Author

[avi2614](https://github.com/avi2614)
