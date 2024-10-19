import folium
import streamlit as st
from streamlit_folium import st_folium
from folium.plugins import Search

def float_input(feature_name, allowed_values):
    """
    Displays a number input widget to capture floating-point input from the user.
    
    Parameters:
    - feature_name (str): The label for the input field displayed in the UI.
    - allowed_values (dict): A dictionary containing 'min' and 'max' as keys for the allowable range:
        - 'min' (float): The minimum floating-point value allowed.
        - 'max' (float): The maximum floating-point value allowed.

    Returns:
    - feature (float): The floating-point number input by the user.
    """

    min_value = allowed_values['min']
    max_value = allowed_values['max']

    feature = st.number_input(feature_name,
                              min_value=min_value,
                              max_value=max_value,
                              format="%.8f")
    return feature

def integer_input(feature_name, allowed_values):
    """
    Displays a number input widget to capture integer input from the user.
    
    Parameters:
    - feature_name (str): The label for the input field displayed in the UI.
    - allowed_values (dict): A dictionary containing 'min' and 'max' as keys for the allowable range:
        - 'min' (int): The minimum integer value allowed.
        - 'max' (int): The maximum integer value allowed.

    Returns:
    - feature (int): The integer number input by the user.
    """

    min_value = allowed_values['min']
    max_value = allowed_values['max']

    feature = st.number_input(feature_name,
                              min_value=min_value,
                              max_value=max_value)
    return feature

def selectbox(feature_name, allowed_values):
    """
    Displays a select box widget to allow the user to choose from a list of predefined options.
    
    Parameters:
    - feature_name (str): The label for the select box displayed in the UI.
    - allowed_values (list): A list of options to be displayed in the select box.

    Returns:
    - feature: The option selected by the user from the dropdown.
    """

    options_to_select = []

    for allowed_value in allowed_values:
        options_to_select.append(allowed_value)

    feature = st.selectbox(feature_name,
                           options=options_to_select)

    return feature

def date_input(feature_name, allowed_values):
    """
    Displays a date input widget to allow the user to select a date.
    
    Parameters:
    - feature_name (str): The label for the date input displayed in the UI.
    - allowed_values: (Unused parameter; exists for compatibility purposes).

    Returns:
    - feature (datetime.date): The date selected by the user.
    """

    feature = st.date_input(feature_name)

    return feature

def time_input(feature_name, allowed_values):
    """
    Displays a time input widget to allow the user to select a time.
    
    Parameters:
    - feature_name (str): The label for the time input displayed in the UI.
    - allowed_values: (Unused parameter; exists for compatibility purposes).

    Returns:
    - feature (datetime.time): The time selected by the user.
    """

    feature = st.time_input(feature_name)

    return feature


def map_input(map_center_coordinates):
    """
    Displays a map input widget to allow the user to select a time.
    
    Parameters:
    - map_center_coordinates (arr): Latitude and Longitude coordinates to load default map location.
    """

    map_widget = folium.Map(location = map_center_coordinates, zoom_start = 12)

    map_widget.add_child(folium.LatLngPopup())

    map_data = st_folium(map_widget, width=1200, height=500)

    if map_data["last_clicked"] is not None:
        lat, lon = map_data["last_clicked"]["lat"], map_data["last_clicked"]["lng"]

        col = st.columns(2)
        with col[0]:
            feature = st.number_input('Easting',
                                      value=lat)
        with col[1]:

            feature = st.number_input('Northing',
                                      value=lon)
    else:
        st.write("Click on the map to get the coordinates")