# Predictive Analysis for Manufacturing Operations 

## Overview
This API is designed to predict machine downtime or production defects using a simple predictive analysis model. The endpoints allow you to upload data, train a model, and make predictions based on input parameters like temperature and runtime.

## Dataset
- A synthetic dataset has been generated with the following key columns:
  - `Machine_ID`
  - `Temperature`
  - `Run_Time`
  - `Downtime_Flag`

## Setup & Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/hmairaj94/Predictive-Analysis-for-Manufacturing-Operations.git
   ```

2. **Create a Virtual Environment**  
   ```bash
   conda activate /apienv
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
```

## API Endpoints

### 1. **Upload Endpoint** (`/upload`)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/upload`
- **Description**: Upload a CSV file containing manufacturing data.
- **Request**: Upload a CSV file (e.g., containing columns `Machine_ID`, `Temperature`, `Run_Time`, `Downtime_Flag`).
- **Response**:
  ```json
  { "message": "File uploaded successfully", "columns": ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"] }
  ```

### 2. **Train Endpoint** (`/train`)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/train`
- **Description**: Train the machine learning model on the uploaded dataset.
- **Request**: No body required.
- **Response**:
  ```json
  { "message": "Model trained successfully", "accuracy": 0.85 }
  ```

### 3. **Predict Endpoint** (`/predict`)
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/predict`
- **Description**: Predict downtime based on input data.
- **Request**:
  ```json
  { "Temperature": 80, "Run_Time": 120 }
  ```
- **Response**:
  ```json
  { "Downtime": 0, "Confidence": 0.85 }
  ```


Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to test the API.

