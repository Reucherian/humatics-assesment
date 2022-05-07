import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("data.csv")
data_vel = data.copy()
data_vel["velocity [m/s]"] = data_vel["velocity [m/s]"].interpolate(method="linear")
x = st.slider("Show velocity till",0,len(data_vel))
fig,ax = plt.subplots()
ax.plot(data_vel["time [s]"][:x],data_vel["velocity [m/s]"][:x])
st.pyplot(fig)