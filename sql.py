from openai import OpenAI
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # Load all the environment variables

# Configure OpenAI API Key
client = OpenAI()

# Function to get response from OpenAI model


def get_openai_response(question, prompt):
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": prompt[0]},
            {"role": "user", "content": question}
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

# Function to run the SQL query


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


# Prompt to guide the model
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENT and has the following columns:
    ID (integer, primary key), NAME (string), CLASS (string), SECTION (string),
    AGE (integer), EMAIL (string), ENROLL_DATE (date).

    For example:
    Example 1 - How many entries of records are present?  
    SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all the students studying in Data Science class?  
    SELECT * FROM STUDENT WHERE CLASS = "Data Science";

    Example 3 - List names and emails of students older than 22.  
    SELECT NAME, EMAIL FROM STUDENT WHERE AGE > 22;

    Example 4 - How many students enrolled after February 1, 2023?  
    SELECT COUNT(*) FROM STUDENT WHERE ENROLL_DATE > '2023-02-01';

    Your response must only include the SQL query.
    Do not include the word 'SQL', markdown, or code blocks.
    """
]


# Streamlit UI
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("OpenAI SQL Assistant")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# If submit is clicked
if submit:
    sql_query = get_openai_response(question, prompt)
    print("Generated SQL:", sql_query)

    try:
        response = read_sql_query(sql_query, "test.db")
        st.subheader("The Response is")
        st.write(sql_query)
        for row in response:
            st.write(row)
    except Exception as e:
        st.error(f"Error executing SQL: {e}")
