# ChurnIQ 🚀

![ChurnIQ](https://img.shields.io/badge/ChurnIQ-ML%20Churn%20Prediction-blue)

Welcome to ChurnIQ, a full-stack application designed to predict customer churn using machine learning. Built with FastAPI, React/TypeScript, and scikit-learn, ChurnIQ provides an interactive user interface and a robust REST API to deliver accurate churn probability predictions. 

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Releases](#releases)

## Features

- **Machine Learning Model**: Utilizes logistic regression to predict churn probability.
- **REST API**: Easily integrates with other applications and services.
- **Interactive UI**: Built with React and TypeScript for a seamless user experience.
- **Data Visualization**: Displays churn predictions and insights clearly.
- **Docker Support**: Simplifies deployment and scaling.
- **Cross-Platform**: Works on any platform that supports Docker.

## Technologies Used

- **Backend**: FastAPI, Python, scikit-learn
- **Frontend**: React, TypeScript
- **Database**: SQLite (or your preferred database)
- **Containerization**: Docker
- **Version Control**: GitHub

## Installation

To get started with ChurnIQ, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/harshmriduhash/ChurnIQ.git
   cd ChurnIQ
   ```

2. **Set up the backend**:
   - Navigate to the backend directory:
     ```bash
     cd backend
     ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set up the frontend**:
   - Navigate to the frontend directory:
     ```bash
     cd ../frontend
     ```
   - Install the required packages:
     ```bash
     npm install
     ```

4. **Run the application**:
   - Start the backend server:
     ```bash
     cd ../backend
     uvicorn main:app --reload
     ```
   - Start the frontend server:
     ```bash
     cd ../frontend
     npm start
     ```

Your application should now be running locally!

## Usage

To use ChurnIQ, follow these steps:

1. Open your browser and navigate to `http://localhost:3000` to access the interactive UI.
2. Input customer data into the form.
3. Click the "Predict" button to see the churn probability.
4. Review the visualizations and insights provided.

For more advanced users, you can interact with the REST API directly. The API documentation is available below.

## API Documentation

ChurnIQ provides a REST API for accessing churn predictions programmatically. Below are the main endpoints:

### Predict Churn

- **Endpoint**: `/api/predict`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "customer_data": {
      "feature1": value,
      "feature2": value,
      ...
    }
  }
  ```
- **Response**:
  ```json
  {
    "churn_probability": value,
    "prediction": "churn" or "not churn"
  }
  ```

### Get Model Info

- **Endpoint**: `/api/model`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "model_name": "Logistic Regression",
    "accuracy": value,
    "features": ["feature1", "feature2", ...]
  }
  ```

## Contributing

We welcome contributions to ChurnIQ! If you'd like to help, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Open a pull request with a clear description of your changes.

## License

ChurnIQ is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to the maintainers:

- **Maintainer Name**: Your Name
- **Email**: your.email@example.com

## Releases

To download the latest version of ChurnIQ, visit our [Releases](https://github.com/XxsebalinkxX/ChurnIQ/releases) section. You can find the necessary files to download and execute the application there.

---

Thank you for your interest in ChurnIQ! We hope you find it useful in predicting customer churn and improving your business strategies.