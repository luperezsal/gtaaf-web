# app.py
import joblib
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
import yaml

from mixins.build_selectors import build_front_inputs
from mixins.input_types import map_input

from utils.transformations import transform_data_into_matrix




PROFILE_IMAGE_PATH = '/media/luis/9C33-6BBD/Drive/IMG_1006.jpg'
GTAAF_IMAGE_PATH = './icons/gtaaf-logo.png'

LINKEDIN_PROFILE = {'name': 'Luis Pérez-Sala García-Plata',
                    'url': 'https://www.linkedin.com/in/luis-p%C3%A9rez-sala-garc%C3%ADa-plata/'}

FIRST_PAPER = { 'name': """Deep learning model of convolutional neural networks
                           powered by a genetic algorithm for prevention of traffic
                           accidents severity""",
                'url': 'https://www.sciencedirect.com/science/article/pii/S0960077923001467?via%3Dihub'}

CONGRESS_PAPER = { 'name' : """Increasing the Accuracy of a Deep Learning Model
                               for Traffic Accident Severity Prediction by Adding
                               a Temporal Category""",
                    'url': 'https://link.springer.com/chapter/10.1007/978-3-031-56950-0_10'}


with open('countries_features/madrid.yaml', 'r') as file:
    country_categories = yaml.safe_load(file)


# Load the pickled models and keras model

#model = load_model('models/madrid.h5')

# Function to predict
@st.cache_data
def predict(model, scaler, encoder, features):
    # Scale the features
    scaled_features = scaler.transform(features)

    # Predict using the Neural Network model
    prediction = model.predict(scaled_features)
    
    # Return the class with the highest probability
    return np.argmax(prediction, axis=1)

# Title of the app

# Instructions

#st.write(f"[{FIRST_PAPER['name']}]({FIRST_PAPER['url']})")
#st.write(f"[{CONGRESS_PAPER['name']}]({CONGRESS_PAPER['url']})")


with st.sidebar:

    left_co, cent_co,last_co = st.columns(3)
    with left_co:
        st.image(GTAAF_IMAGE_PATH, width=275)
        
    # st.write(f"[{LINKEDIN_PROFILE['name']}]({LINKEDIN_PROFILE['url']})")
    #st.title("Accident Features")
    #st.write("Select the accident features to predict his need of assistance")
    features_inputs = build_front_inputs(country_categories)

#st.image(GTAAF_IMAGE_PATH, use_column_width='always')
st.title("General model for Traffic Accident Assistance Forecasting")


map_center_coordinates = [40.416775, -3.703790]  # Madrid coordinates

map_input(map_center_coordinates)

# Arrange the features as an array
features = np.array([[features_inputs]])

# Get the prediction
#prediction = predict(model, scaler, encoder, features)

# Display the prediction
st.subheader("Prediction:")
#st.write(['setosa', 'versicolor', 'virginica'][prediction[0]])