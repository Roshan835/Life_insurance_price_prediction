# Life_insurance_price_prediction
End to end project on life insurance price prediction

# ML Model Deployment with Flask

This project demonstrates how to deploy a machine learning model using Flask to create a simple web application for making predictions.

## Project Structure

The project is organized as follows:

- `app.py`: The main Flask application that handles web requests and model predictions.
- `model.py`: Contains functions for training and making predictions using a machine learning model.
- `requirements.txt`: Contains all the required libraries.
- `templates/`: Directory for HTML templates used in the web application.
  - `index.html`: The main HTML template for the web app's user interface.

## Getting Started

Follow these steps to set up and run the project:

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd ml-model-deployment-flask
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    virtualenv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**

    ```bash
    python app.py
    ```

    The web app will be accessible at `http://localhost:8080`.

## Usage

1. Open your web browser and navigate to `http://localhost:8080`.

2. Enter a values in the input field and click the "Predict" button.
