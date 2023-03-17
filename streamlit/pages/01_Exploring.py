from tkinter import Image
import streamlit as st


st.header("Exploring the Commercial Environment: How Business Surroundings Impact Success")

st.markdown("""
To get a better understanding of what makes a successful Interrapidisimo branch, I started by collecting data using Google Maps API. I focused on three major Colombian cities - Bogota, Medellin, and Cali - and created six data frames containing information about Interrapidisimo branches and their competitor, Servientrega. For each city, I had a data frame for both companies, including details like Name, Latitude, Longitude, Number of Reviews, and Address.
""")
st.image("imagens/df1.png", width=700)

("""Now, finding demographic data in Colombia can be a bit tricky, so I had to think outside the box. I manually added socio-economic strata (Estratos) for each address, which helped me create a function to calculate the average income in US dollars for each stratum. This information was then added to my data frames in a new column called average_inc_us.
""")

st.image("imagens/ave_inc.png", width=400, caption="Average Income per Stratum")

st.markdown("""
I realized the value of looking at the local business environment as I set out to comprehend the elements that contribute to a successful Interrapidisimo branch. The performance and customer base of a branch can be greatly impacted by the existence of different types of businesses nearby.

""")
st.image("imagens/map2.png", width=600)

st.markdown("""
By gathering this data, I hope to evaluate how each franchise's performance is impacted by the local business environment. This research will assist me in locating patterns and trends that may help me decide where to locate a new Interrapidisimo branch in Cali, Colombia. By taking into account both the demographics and the commercial dynamics of the region, I can optimize my decision to increase the chances of success for the new branch.
""")
st.image("imagens/map1.png", width=600)