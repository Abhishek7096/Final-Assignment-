# app.py
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title('Machine Learning Task Application')

# Sidebar for user input
st.sidebar.header('User Input')
data_option = st.sidebar.selectbox('Choose data source', ['Iris Dataset', 'Upload CSV', 'Enter Data Manually'])

if data_option == 'Iris Dataset':
    data = load_iris(as_frame=True).frame
elif data_option == 'Upload CSV':
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
elif data_option == 'Enter Data Manually':
    st.sidebar.write('Enter your data manually')
    num_rows = st.sidebar.number_input('Number of rows', min_value=1, value=5)
    num_cols = st.sidebar.number_input('Number of columns', min_value=1, value=4)
    data = pd.DataFrame(np.random.randn(num_rows, num_cols), columns=[f'Column {i+1}' for i in range(num_cols)])

if data is not None:
    st.write('Data Preview:')
    st.write(data.head())
    
    # Example ML Task: Classify Iris species
    if data_option == 'Iris Dataset':
        X = data.drop('target', axis=1)
        y = data['target']
    else:
        X = data
        y = st.sidebar.text_input('Enter target column name')
        y = data[y] if y in data.columns else None
    
    if y is not None:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        clf = RandomForestClassifier()
        clf.fit(X_train, y_train)
        accuracy = clf.score(X_test, y_test)
        st.write(f'Model Accuracy: {accuracy:.2f}')
