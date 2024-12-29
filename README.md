# CatPic Pipeline

A fun, end-to-end demonstration of **Continuous Integration / Continuous Delivery (CI/CD)** using Jenkins, Docker, and a simple Python/Flask application that displays random cat pictures via [The Cat API](https://thecatapi.com/).

## Overview

- **App**: A minimal Flask server (`app.py`) that fetches random cat pictures from a public API.
- **Testing**: Simple unit tests (using `pytest`) to ensure the server behaves as expected.
- **Docker**: Containerises the app with a `Dockerfile` for reproducible builds and deployment.
- **Jenkins**: Automates the pipeline (build → test → build Docker image → push to registry → optional deployment).

## Features
1. **Random Cat Images**: The Flask app fetches images from The Cat API and displays them on the home page.
2. **Simple Tests**: Ensures the home route returns a `200 OK` status.
3. **Docker Container**: Quick to spin up anywhere, from local dev to production.
4. **Jenkins Pipeline**: Declarative pipeline pulling code from this Git repository, installing dependencies, running tests, then building and pushing a Docker image.

---

## Getting Started

### Prerequisites
- **Python 3.9+**
- **Pip** or another package manager (e.g. Pipenv, Poetry)
- **Docker** (if you want to build/run the container)
- **Jenkins** (optional, if you want to replicate the full CI/CD pipeline locally)

### 1. Clone the Repo

    git clone git@github.com:miketigerblue/CatPic-Pipeline.git
    cd CatPic-Pipeline

### 2. Set Up a Virtual Environment (Optional But Recommended)
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Run the Flask App Locally
    python app.py
    The server defaults to http://127.0.0.1:5000.
    Press CTRL+C to stop the server.

### 5. Run Tests
    pytest --maxfail=1 --disable-warnings -q

A passing test indicates the route / returns a 200 OK.

## Docker Usage

Build the Docker Image

    docker build -t catpicapp:latest .

Run the Container

    docker run -d -p 5000:5000 --name catpicapp catpicapp:latest

After starting, open http://localhost:5000 to see your random cat pics.

Stop & Remove the Container

    docker stop catpicapp
    docker rm catpicapp

## Jenkins CI/CD

Jenkinsfile

The Jenkinsfile defines a Declarative Pipeline with stages:

- **Checkout**: Clones this repo from GitHub.
- **Install Dependencies**: Installs required Python libraries.
- **Test**: Runs the unit tests in tests/test_app.py.
- **Build Docker Image**: Builds the Docker image catpicapp.
- **Push to Docker Registry** (Optional): Pushes the image to your Docker registry of choice.
- **Deploy** (Optional): Runs the container, or you can replace this stage with a deploy to a Docker host, Kubernetes, etc.
- **Post Actions**: Slack or email notifications on success/failure (configure in Jenkins settings).

## Configuring Jenkins

- Create a New Pipeline in Jenkins, pointing to your Git repo.
- Supply credentials if needed (e.g. GitHub SSH key, Docker Hub credentials).
- Adjust environment variables in the Jenkinsfile if you want to push to a Docker registry.
- Build and watch the magic happen in the Jenkins console logs.


# CatPic-Pipeline
