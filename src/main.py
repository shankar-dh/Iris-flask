from flask import Flask, request, jsonify
from predict import predict_iris

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Get the input features from the request
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    print(sepal_length, sepal_width, petal_length, petal_width)

    # Make predictions using the trained model
    prediction = predict_iris(sepal_length, sepal_width, petal_length, petal_width)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)