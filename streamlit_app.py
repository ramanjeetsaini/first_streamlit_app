import streamlit
import pandas
import requests
import snowflake.connector

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


streamlit.title('My Parents new healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🐔 Butter Chicken')
streamlit.text('🥣 Dal Tadka')
streamlit.header(' Build your own smoothie')
streamlit.dataframe(my_fruit_list)
my_fruit_list = my_fruit_list.set_index('Fruit')

#putting a pickup list to pick fruits they want to include
fruits_selected = streamlit.multiselect("Pick some fruits",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json())
fruit_choice = streamlit.text_input('What fruit would like information about?','Kiwi')
streamlit.write('the user entered', fruit_choice)


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
my_data_row = my_cur.fetchall()
streamlit.text("THE FRUIT LOAD LIST CONTAINS: ")
streamlit.dataframe(my_data_row)

add_my_fruit = streamlit.text_input("What fruit would you like to add? ")
streamlit.write("Thanks for adding:", add_my_fruit)
my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ('",add_my_fruit,"')")
