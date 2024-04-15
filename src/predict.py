import numpy as np
import joblib
import os
from train import run_training

# Load the trained model
model = joblib.load("model/model.pkl")

def predict_iris(sepal_length, sepal_width, petal_length, petal_width):
    # Create a numpy array with the input features
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make predictions using the trained model
    prediction = model.predict(input_data)

    return prediction[0]

if __name__ == "__main__":
    if os.path.exists("model/model.pkl"):
        print("Model loaded successfully")
    else:
        os.makedirs("model", exist_ok=True)
        run_training()
