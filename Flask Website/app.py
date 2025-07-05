from flask import Flask, request, render_template
import pickle
import numpy as np
import pandas as pd

# Load the trained XGBoost model
with open("XGBoost.pkl", "rb") as file:
    model = pickle.load(file)

# Load the feature columns
with open("feature_columns.pkl", "rb") as file:
    feature_columns = pickle.load(file)

# Load the scaler
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)
    
# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return render_template('home.html')

# Define the prediction route
@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    if request.method == "POST":
        try:
            # Collect input data from the form
            distrik = request.form["distrik"]
            kota = request.form["kota"]
            kamar = int(request.form["kamar"])
            kamar_mandi = int(request.form["kamar_mandi"])
            area = float(request.form["area"])
            size = float(request.form["size"])
            lantai = int(request.form["lantai"])
            garasi = int(request.form["garasi"])

            # Create a DataFrame for the input data
            input_data = pd.DataFrame([{
                "distrik": distrik,
                "kota": kota,
                "kamar": kamar,
                "kamar_mandi": kamar_mandi,
                "area": area,
                "size": size,
                "lantai": lantai,
                "garasi": garasi
            }])

            # Perform one-hot encoding for distrik and kota
            input_data = pd.get_dummies(input_data, columns=['distrik', 'kota'], drop_first=True)

            # Ensure input_data has the same columns as the training data
            input_data = input_data.reindex(columns=feature_columns, fill_value=0)

            # Normalize the input data using the scaler
            input_data_scaled = scaler.transform(input_data)
            
            # Make prediction and inverse log transformation
            prediction_log = model.predict(input_data_scaled)[0]
            prediction = np.expm1(prediction_log)  # Inverse log transformation
            prediction = f"Rp {prediction:,.0f}"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template('predict.html', prediction=prediction)

# Login route
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)