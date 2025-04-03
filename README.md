# Predicción de Precios de Casas

Este proyecto es una aplicación web que permite predecir el precio de una casa en función de sus características. Utiliza un modelo de Machine Learning implementado en Flask para hacer las predicciones.

## Tecnologías Utilizadas
- Python (Flask, Scikit-learn, Pandas)
- HTML, CSS
- Jupiter Notebook
- Fetch API para la comunicación con Flask

## Instalación y Configuración
### 1. Clonar el repositorio
```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
```

### 2. Crear un entorno virtual (opcional pero recomendado)
```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
    pip install -r requirements.txt
```

### 4. Ejecutar la API Flask
Usa un servidor local para servir index.html

Ejecuta un servidor HTTP simple para servir el archivo index.html. Por ejemplo:

Abre una terminal en el directorio donde está index.html.
Ejecuta el siguiente comando (asegúrate de tener Python instalado):
Abre tu navegador y ve a 
http://127.0.0.1:8000/index.html.
Por defecto, Flask correrá en `http://127.0.0.1:5000`.

### 5. Ejecutar la aplicación web
Abre el archivo `index.html` en tu navegador.

## Uso de la Aplicación
1. Completa el formulario con los datos de la vivienda.
2. Haz clic en "Predecir Precio".
3. La aplicación enviará los datos a la API Flask y mostrará el precio estimado.

![pagina_casas](https://github.com/user-attachments/assets/9d7f4b0c-918d-48a2-9d88-f6aea4fb6eb2)



## API Endpoint
### `POST /predict`
- **Entrada:** JSON con los datos de la casa.
- **Salida:** Precio estimado.

Ejemplo de solicitud:
```json
{
    "area": 2000,
    "bedrooms": 3,
    "bathrooms": 2,
    "stories": 1,
    "mainroad": 1,
    "guestroom": 0,
    "basement": 1,
    "hotwaterheating": 0,
    "airconditioning": 1,
    "parking": 2,
    "prefarea": 0,
    "furnishingstatus_furnished": 0,
    "furnishingstatus_semi-furnished": 1,
    "furnishingstatus_unfurnished": 0
}
```

Ejemplo de respuesta:
```json
{
    "prediction": 150000.0
}
```


