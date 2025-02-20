import streamlit as st
import joblib
import pandas as pd
import numpy as np
from io import BytesIO
import patoolib

# Load the machine learning model
model = joblib.load('random_forest.joblib')

# Extract the RAR file
patoolib.extract_archive('dataset_pre-processed.rar', outdir='.')

# Read the contents
preprocessed_data = pd.read_csv('dataset_pre-processed.csv')

# Load the preprocessor
preprocessor = joblib.load('pre_processor.joblib')

def show_machine_learning_page():
    st.title('Machine Learning Predictions')

    selected_region = st.selectbox('Select a Region', preprocessed_data['Region'].unique())

    # Extract year and month from 'Date' column 
    preprocessed_data['Year'] = pd.to_datetime(preprocessed_data['Date']).dt.year
    preprocessed_data['Month'] = pd.to_datetime(preprocessed_data['Date']).dt.month

    # User selects a year and month from the dropdown
    selected_year = st.selectbox('Select a Year', preprocessed_data['Year'].unique())
    selected_month = st.selectbox('Select a Month', preprocessed_data['Month'].unique())

    # Filter the dataset based on the selected region, year, and month
    filtered_data = preprocessed_data[
        (preprocessed_data['Region'] == selected_region) &
        (preprocessed_data['Year'] == selected_year) &
        (preprocessed_data['Month'] == selected_month)
    ]

    if st.button('Predict'):
        # Apply the same preprocessing as during training
        input_data_preprocessed = preprocessor.transform(filtered_data)

        # Make prediction
        predictions = model.predict(input_data_preprocessed)

        # Calculating the average prediction
        avg_prediction = np.mean(predictions)

        # Displaying the prediction method
        st.markdown('**Prediction made using Random Forest Model:**')

        st.markdown(f'<h2 style="font-weight:bold; color:blue;">Average Predicted Energy Consumption for {selected_region} in {selected_year} for the Month {selected_month} (MW):</h2>', unsafe_allow_html=True)
        st.markdown(f'<h1 style="font-weight:bold; color:#FF4B4B;">{avg_prediction:.2f}</h1>', unsafe_allow_html=True)

        # Additional contextual information
        st.write(f'Based on {len(filtered_data)} data points from {selected_year} in the Month {selected_month}.')
