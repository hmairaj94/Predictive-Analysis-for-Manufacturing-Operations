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
   python -m venv venv
   source venv/bin/activate
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

Here’s how you can test the API endpoints using Postman:

### 1. **Upload Endpoint (`/upload`)**
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/upload`
- **Body**: Select **form-data** and choose **File** type for your file input. Choose a `.csv` file.
- **Response**: 
  ```json
  { "message": "File uploaded successfully", "columns": ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"] }
  ```

### 2. **Train Endpoint (`/train`)**
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/train`
- **Body**: None
- **Response**: 
  ```json
  { "message": "Model trained successfully", "accuracy": 0.85 }
  ```

### 3. **Predict Endpoint (`/predict`)**
- **Method**: `POST`
- **URL**: `http://127.0.0.1:8000/predict`
- **Body**: Select **raw** and choose **JSON**. Input JSON data:
  ```json
  { "Temperature": 80, "Run_Time": 120 }
  ```
- **Response**: 
  ```json
  { "Downtime": 0, "Confidence": 0.85 }
  ```

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to test the API.
![Screenshot (78)](https://github.com/user-attachments/assets/4d2f41b4-1d80-44b8-9200-7f771c819fdc)
![Screenshot (79)](https://github.com/user-attachments/assets/2843c362-5c4a-4ecb-9bac-de5a09614c32)
![Screenshot (80)](https://github.com/user-attachments/assets/fb69bebb-792e-4eae-8ec9-e95bc1dc3709)
![Screenshot (81)](https://github.com/user-attachments/assets/8adfeac3-9be2-422a-a8d9-a06025f24dbf)


