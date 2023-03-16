from tkinter import Image
import streamlit as st


st.markdown("### **Unlocking the Mysteries of Interrapidisimo Performance: A Dive into Correlations**")

st.write("""
In order to conduct a more thorough investigation of possible correlations, I chose to create dummy variables for the different kinds of businesses that are located close to the Interrapidisimo branches. I was able to explore the complex connections between the commercial environment and the top-performing Interrapidisimo branches by conducting this analysis particularly for the best_inter data frame.
""")

st.image("imagens/type.png", width=600)

st.write("""
To achieve this, I created two correlation matrices - one based on the Number of Reviews and another on the Rating. This approach allowed me to examine the complex relationships between the performance of Interrapidisimo branches and various factors, such as the types of businesses in the surrounding area and demographic characteristics.
""")

st.image("imagens/rev_corr.png", width=600)

st.write("""
I observe an interesting negative correlation (-0.387426) between the number of reviews and socioeconomic class. This indicates that lower-stratum neighborhoods tend to have branches with more reviews, possibly as a result of these communities' higher population densities. In these busy areas, there is more opportunity for customer interaction, which fosters a favorable atmosphere for obtaining more reviews.
""")


st.write("""
Also, the research found a fascinating positive association (0.658051) between the quantity of reviews and population density. According to this correlation, branches located in densely populated areas are more likely to obtain positive reviews. These lively places are hubs for gathering customer input because of the increased foot traffic and customer interaction.
""")
st.image("imagens/scatter1.png", width=600)


st.write("""
Based on the correlations observed scatter plot, it can be concluded that the success of Interrapidísimo franchises in Cali, Medellín, and Bogotá seems to be influenced by certain factors. The population density and presence in lower socioeconomic strata neighborhoods suggest that the demand for shipping services might be higher in these areas, which could explain the higher number of reviews. Additionally, the presence of fewer competitors and a lower concentration of services in the area could indicate that Interrapidísimo has a competitive advantage in these locations.
""")
st.image("imagens/scatter2.png", width=600)

st.write("""
We can interpret the negative correlation found between the "Number of Reviews" and "Estratos" and "average_inc_us" variables as indicating that Intterapidísimo franchises located in areas with lower socioeconomic status and lower average income are more likely to receive more reviews. This could suggest that the franchise's pricing may be more appealing to customers in these areas, leading to more frequent use and more opportunities to leave reviews. Additionally, it may be easier for individuals or small businesses in lower-income areas to use Intterapidísimo for sending packages, leading to more reviews from those areas.
""")