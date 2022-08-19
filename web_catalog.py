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
# streamlit.write(df)

# put the styles/colors into a list
color_list = df[0].values.tolist()

# put the color_list into a pick box
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

# picture caption
product_caption = f"Our warm, comfortable, {option} sweatsuite!"

# Get more product data
select_str = f"""SELECT direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '{option}';"""
cur.execute(select_str)
details_df = cur.fetchone()

streamlit.image(details_df[0], width=400, caption=product_caption)

streamlit.write('Price', details_df[1])
streamlit.write('Sizes Available',details_df[2])
streamlit.write(details_df[3]
