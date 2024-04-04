# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title("My Parents New Healthy Diner")
st.write(
    """ **Breakfast Menu**
          Omega 3 & Blueberry Oatmeal
	  Kale, Spinach and Rocket Smoothie
          Hard-Boiled Free Range Egg
    """
)


#this part of this code is no longer needed
#option = st.selectbox(
#    'What is your favourite fruit?',
 #  ('Banana', 'Strawberry', 'Peaches'))

#st.write('Your favourite fruit is:', option)

from snowflake.snowpark.functions import col

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:'
    , my_dataframe
)

if ingredients_list:
    #st.write(ingredients_list)
    #st.text(ingredients_list)
    ingredients_string = ''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
            values ('""" + ingredients_string + """')"""

    #st.write(my_insert_stmt)
    time_to_insert = st.button('Submit Order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
	
        st.success('Your Smoothie is ordered!', icon="✅")

cnx = st.connection("snowflake")
session = cnx.session()
