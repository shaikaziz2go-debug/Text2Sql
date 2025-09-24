from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai
#config api key
genai.configure(api_key=os.getenv("API_KEY"))

## Function to load google model and load sql database
def load_model(question,prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, question])
    
    return response.text

def load_database(sql,db):
    connection=sqlite3.connect(db)
    cursor=connection.cursor()
    # Clean the SQL string by removing Markdown syntax
    sql_clean = sql.replace('```sql', '').replace('```', '').strip()

    data=cursor.execute(sql_clean)
    result=data.fetchall()
    connection.commit()
    connection.close()
    return result
    for row in data:
        print(row)
        return row

# Providing prompt to the model
prompt="You are a SQL expert. You will be given a question and a database table. You need to generate the SQL query to answer the question based on the database table. Only provide the SQL query as output. Do not provide any explanation or additional text. The database table is named 'Student' and has the following columns: ID (INTEGER), Name (TEXT), Age (INTEGER), marks (INTEGER), section (TEXT)."

# Streamlit app
st.title("Text to SQL Query using Gemini Pro")
st.write("Enter a question related to the Student database and get the SQL query and result.")

question = st.text_input("Question:")
if st.button("Submit"):
    sql_query = load_model(question, prompt)
    st.write("SQL Query:")
    st.code(sql_query)
    st.write("Result:")
    result = load_database(sql_query, 'Student.db')
    st.subheader("The result is:")
    for row in result:
        st.write(row)