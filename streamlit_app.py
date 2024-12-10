import streamlit as st
from supabase import create_client, Client


st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# Initialize connection.
# Uses st.cache_resource to only run once.
# @st.cache_resource
# def init_connection():
#     supabase_config = st.secrets["connections"]["supabase"]
#     url = supabase_config["SUPABASE_URL"]
#     key = supabase_config["SUPABASE_KEY"]
#     return create_client(url, key)

# supabase = init_connection()

# # Perform query.
# # Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
# def run_query():
#     return supabase.table("mytable").select("*").execute()

# rows = run_query()

# # Print results.
# for row in rows.data:
#     st.write(f"{row['name']} has a :{row['pet']}:")