import streamlit as st
from mixins.input_types import *


def build_front_inputs(country_categories):

    features_inputs = []

    for country_category, country_features in country_categories.items():

        st.header(country_category)

        elements_by_row = country_features['elements_by_row']

        columns = st.columns(elements_by_row)

        for feature_number, country_feature in enumerate(country_features['features']):
 
            with columns[feature_number % elements_by_row]:

                for feature_name, properties in country_feature.items():

                    input_type = properties['input_type']
                    allowed_values = properties['allowed_values']

                    build_front_input = globals().get(f"{input_type}")

                    if callable(build_front_input):
                        feature_input = build_front_input(feature_name, allowed_values)
                        features_inputs.append(feature_input)

    return features_inputs
