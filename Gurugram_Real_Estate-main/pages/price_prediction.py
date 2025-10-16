import streamlit as st
import pickle
import pandas as pd
import numpy as np
import joblib

with open('df.pkl','rb') as file:
    df=pickle.load(file)

with open('pipeline.pkl','rb') as file:
    pipeline = joblib.load("pipeline.pkl")


# st.dataframe(df)
st.header("Enter your inputs")
property_type=st.selectbox('property Type',['flat','house'])
sectors= st.selectbox('sector',sorted(df['sector'].unique().tolist()))
Bedrooms= float(st.selectbox('Number of bedrooms',sorted(df['bedRoom'].unique().tolist())))
Bathrooms= float(st.selectbox('Number of bathrooms',sorted(df['bathroom'].unique().tolist())))
Balcony=st.selectbox('Number of balconies',sorted(df['balcony'].unique().tolist()))
property_age=st.selectbox('Property age',sorted(df['agePossession'].unique().tolist()))
Built_up_area=float(st.number_input('built_up_area'))
servant_room= float(st.selectbox('servant Room',[0.0,1.0]))
store_room= float(st.selectbox('store Room',[0.0,1.0]))
furnishing_type=st.selectbox('Furnishing_type',sorted(df['furnishing_type'].unique().tolist()))
luxury_category=st.selectbox('Luxury_category',sorted(df['luxury_category'].unique().tolist()))
floor_category=st.selectbox('Floor_category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):

    data = [[property_type,sectors, Bedrooms, Bathrooms, Balcony,  property_age,Built_up_area, servant_room, store_room, 
             furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
       'agePossession', 'built_up_area', 'servant room', 'store room',
       'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)
    # st.dataframe(one_df)


    base_price=np.expm1(pipeline.predict(one_df))[0]
    low=base_price-0.22
    high=base_price+0.22

    st.text("The price of the flat or house is between {} Cr and {} Cr".format(round(low,2),round(high,2)))

