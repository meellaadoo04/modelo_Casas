import requests

API_URL = 'http://127.0.0.1:5000/predict'

# Datos base de entrada
input_data_base = {
    'area': 7420,
    'bedrooms': 4,
    'bathrooms': 2,
    'stories': 3,
    'parking': 1,
    'mainroad': 0,
    'guestroom': 0,
    'basement': 0,
    'hotwaterheating': 1,
    'airconditioning': 1,
    'prefarea': 1,
    'furnishingstatus_furnished': 1,
    'furnishingstatus_semi-furnished': 0,
    'furnishingstatus_unfurnished': 0
}

# Calcular las características derivadas
input_data = input_data_base.copy()
input_data['bed_to_bath_ratio'] = input_data['bedrooms'] / input_data['bathrooms']
input_data['area_per_story'] = input_data['area'] / input_data['stories']
input_data['bath_per_story'] = input_data['bathrooms'] / input_data['stories']
input_data['room_density'] = (input_data['bedrooms'] + input_data['bathrooms']) / input_data['area']
input_data['parking_per_area'] = input_data['parking'] / input_data['area']
input_data['bedrooms_per_story'] = input_data['bedrooms'] / input_data['stories']
input_data['bathrooms_per_bedroom'] = input_data['bathrooms'] / input_data['bedrooms']
input_data['area_per_bedroom'] = input_data['area'] / input_data['bedrooms']
input_data['area_per_bathroom'] = input_data['area'] / input_data['bathrooms']
input_data['parking_per_bedroom'] = input_data['parking'] / input_data['bedrooms']

# Orden exacto del entrenamiento
keys_scaler = [
    'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 'basement', 
    'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus_furnished', 
    'furnishingstatus_semi-furnished', 'furnishingstatus_unfurnished', 'bed_to_bath_ratio', 
    'area_per_story', 'bath_per_story', 'room_density', 'parking_per_area', 'bedrooms_per_story', 
    'bathrooms_per_bedroom', 'area_per_bedroom', 'area_per_bathroom', 'parking_per_bedroom'
]

# Crear un nuevo diccionario ordenado según keys_scaler
input_data_ordered = {key: input_data[key] for key in keys_scaler}

# Enviar una solicitud POST a la API
response = requests.post(API_URL, json=input_data_ordered)

# Verificar la respuesta
if response.status_code == 200:
    print(f"Predicted Price: {response.json()['predicted_price']}")
else:
    print(f"Error: {response.json()['error']}")

