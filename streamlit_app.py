import streamlit
import pandas

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
