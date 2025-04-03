from flask import Flask, request, jsonify, Blueprint
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from flask_cors import CORS

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)  # Permitir todas las solicitudes CORS

# Crear el Blueprint
routes = Blueprint('routes', __name__)

# Cargar el modelo y los escaladores
model = load_model('best_model.keras')
scaler = joblib.load('scaler_X.joblib')
scaler_precio = joblib.load('scaler_y.joblib')

@routes.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Orden exacto del entrenamiento
        keys_scaler = [
            'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 
            'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus_furnished', 
            'furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished', 'bed_to_bath_ratio', 
            'area_per_story', 'bath_per_story', 'room_density', 'parking_per_area', 'bedrooms_per_story', 
            'bathrooms_per_bedroom', 'area_per_bedroom', 'area_per_bathroom', 'parking_per_bedroom'
        ]
        
        scaler_input = [data[key] for key in keys_scaler]
        scaler_input_df = pd.DataFrame([scaler_input], columns=keys_scaler)
        
        scaled_values = scaler.transform(scaler_input_df)[0].tolist()
        print("Scaled values (24):", scaled_values)

        final_features = scaled_values
        prediction_scaled = model.predict(np.array([final_features]))
        prediction_original = scaler_precio.inverse_transform(prediction_scaled)
        
        # Formatear la salida con el símbolo de dólar y separadores de miles
        formatted_price = "${:,.2f}".format(prediction_original[0][0])

        return jsonify({'predicted_price': formatted_price})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Registrar el Blueprint en la aplicación Flask
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)