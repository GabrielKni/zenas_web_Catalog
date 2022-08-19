import streamlit
import snowflake.connector
import pandas

streamlit.title("Zena's Amazing Athleisure Catalog")

# connect to snowflake
conn = snowflake.connector.connect(**streamlit.secrets["snowflake"])
cur = conn.cursor()

# run a snwoflake query and put it all in a car called catalog
select_str = """Select color_or_style from catalog_for_website"""
cur.execute(select_str)
catalog = cur.fetchall()

#put the data into a dataframe
df = pandas.DataFrame(catalog)

# testing dataframe data
streamlit.write(df)
