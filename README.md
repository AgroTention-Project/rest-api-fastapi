# AgroTention Back End RESTFul API

This repository contains the Back End REST API service for **AgroTention**, a plant detection and disease identification platform.

## Table of Contents

- [About AgroTention](#about-agrotention)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

---

## About AgroTention

AgroTention is a solution for farmers and agricultural stakeholders to:

1. Identify diseases affecting crops.
2. Provide actionable insights to improve agricultural productivity.

This project is part of the **Bangkit Capstone Project**, developed by Team **C242-PS073**.

---

## Features

- **Fast and Scalable API**: Built with FastAPI.
- **Cloud Integration**: Uses Google Cloud Platform services such as Firestore and Vertex AI.
- **Disease Detection**: Machine learning models trained on expert-labeled datasets.
- **Structured API Documentation**: Interactive documentation powered by FastAPI.

---

## Technologies Used

- **Framework**: FastAPI
- **Database**: Firestore (NoSQL)
- **Machine Learning**: Vertex AI
- **Deployment**: App Engine (Google Cloud Platform)
- **Programming Language**: Python

---

## Installation

### Prerequisites

- Python 3.12 or later
- Google Cloud SDK
- Firestore credentials

### Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:AgroTention-Project/rest-api-fastapi.git
   cd rest-api-fastapi
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:

   - Create a `.env` file with the following variables:
     ```
     GOOGLE_APPLICATION_CREDENTIALS=<path-to-service-account-json>
     ```

5. Run the application:
   ```bash
   fastapi dev server
   ```

---

## Documentation

### Production
- [SwaggerUI](https://agrotention-project-441716.et.r.appspot.com/docs)
- [Redoc](https://agrotention-project-441716.et.r.appspot.com/redoc)

### Development
- [SwaggerUI](https://development-agrotention-project-441716.et.r.appspot.com/docs)
- [Redoc](https://development-agrotention-project-441716.et.r.appspot.com/redoc)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
