import re
import pandas as pd
import streamlit as st
import subprocess
import base64
from datetime import datetime

# Load the renewable energy and international disaster datasets
renewable_energy_data = pd.read_csv('/Users/pavanjeevanbuddala/Downloads/Econinjas copy/modern-renewable-energy-consumption data.csv')  # Replace with your path
disaster_data = pd.read_excel('/Users/pavanjeevanbuddala/Downloads/Econinjas copy/public_emdat_2024-09-30.xlsx')  # Replace with your path

# Data Preprocessing for renewable energy data
renewable_energy_data['Year'] = pd.to_numeric(renewable_energy_data['Year'], errors='coerce')

# Data Preprocessing for disaster data
disaster_data['Start Year'] = pd.to_numeric(disaster_data['Start Year'], errors='coerce')

# Function to encode an image to base64
# Set the path to your local GIF for background
background_gif_path = '/Users/pavanjeevanbuddala/Downloads/Econinjas copy/emission.jpeg'

# Function to encode GIF as base64
def get_base64_of_bin_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
    return base64.b64encode(data).decode()

base64_background = get_base64_of_bin_file(background_gif_path)

page_bg_img = f'''
<style>
.stApp {{
    background-image: url("data:image/gif;base64,{base64_background}");
    background-size: 100% 100%; /* Ensure the image fits the entire screen without tiling */
    background-repeat: no-repeat; /* Prevent repetition */
    background-position: center; /* Center the background image */
    background-attachment: fixed; /* Make the background fixed during scrolling */
    color: yellow;
    font-family: 'Poppins', sans-serif;
}}

h1 {{
    color: #2C3E50; /* Dark blue color for the title */
    text-align: center;
    font-size: 4em; /* Adjusted font size */
    font-weight: bold;
    margin-bottom: 20px;
}}

p, label {{
    color: #2C3E50; /* Change color for all text to white for better readability */
    font-size: 1.2em; /* Adjust text size */
}}

textarea {{
    font-size: 1em; /* Input box text size */
}}

button {{
    font-size: 1.1em; /* Button text size */
    color: #2C3E50; /* Button text color */
    background-color: #2C3E50; /* Dark blue background for better visibility */
    border: 2px solid black; /* Border with black color */
    padding: 10px 20px; /* Add padding */
    text-align: center; /* Center text */
    text-decoration: none; /* Remove text underline */
    display: inline-block; /* Keep inline display */
    margin: 4px 2px; /* Add margin */
    cursor: pointer; /* Show pointer on hover */
    border-radius: 8px; /* Rounded corners */
}}
button:hover {{
    background-color: #1F2A38; /* Slightly darker shade for hover effect */
    color: #FFD700; /* Change text color to golden yellow on hover */
}}

/* New CSS for making alert box text and Markdown content white */
div.stAlert p, div.stMarkdown p, div.stMarkdown span {{
    color: white !important; /* Ensures all Markdown and alert text is white */
}}

/* Additional style for lists inside Markdown */
div.stMarkdown ul li {{
    color: white !important; /* Change bullet list items to white */
}}
</style>
'''

# Add the CSS to Streamlit
st.markdown(page_bg_img, unsafe_allow_html=True)


# Add the background GIF CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Streamlit App Title
st.title("ClimateGPT: Climate Analysis Chatbot(Llama 3.1)")

# Function to structure chatbot responses
def format_response(title, content):
    return f"""
**{title}**
{content}
"""

# Function to check for small talk
def is_small_talk(text):
    greetings = ["hi", "hello", "how are you", "hey", "good morning", "good evening", "what's up"]
    return any(greet in text.lower() for greet in greetings)

# Function to extract country, year, and type of energy or disaster
def extract_info_from_text(text):
    country_match = None
    country_mapping = { "india": "India", "united states": "United States", "china": "China", "brazil": "Brazil" }  # Add more countries as needed

    for country in country_mapping.keys():
        if re.search(rf"\b{country}\b", text, re.IGNORECASE):
            country_match = country_mapping[country]
            break

    year_match = re.search(r"\b(\d{4})\b", text)
    year = int(year_match.group(0)) if year_match else None

    if "renewable" in text.lower():
        data_type = "renewable"
    elif "disaster" in text.lower():
        data_type = "disaster"
    else:
        data_type = None

    return country_match, year, data_type

# Renewable energy functions
def get_renewable_data(entity, year):
    result = renewable_energy_data[(renewable_energy_data['Entity'] == entity) & (renewable_energy_data['Year'] == year)]
    if not result.empty:
        return result[['Solar_generation_-_twh', 'Wind_generation_-_twh', 'Hydro_generation_-_twh']].to_string(index=False)
    else:
        return None

def generate_energy_summary(entity, year):
    data = renewable_energy_data[(renewable_energy_data['Entity'] == entity) & (renewable_energy_data['Year'] == year)]
    if not data.empty:
        return {
            "Solar (TWh)": data['Solar_generation_-_twh'].sum(),
            "Wind (TWh)": data['Wind_generation_-_twh'].sum(),
            "Hydro (TWh)": data['Hydro_generation_-_twh'].sum()
        }
    else:
        return "No data available for the specified country and year."

# Disaster functions
def get_disaster_data(country, year):
    result = disaster_data[(disaster_data['Country'] == country) & (disaster_data['Start Year'] == year)]
    if not result.empty:
        return result[['Disaster Type', 'Total Affected', 'Total Deaths', 'Total Damage (\'000 US$)']].to_string(index=False)
    else:
        return None

def generate_disaster_summary(country, year):
    data = disaster_data[(disaster_data['Country'] == country) & (disaster_data['Start Year'] == year)]
    if not data.empty:
        return {
            "Total Affected": data['Total Affected'].sum(),
            "Total Deaths": data['Total Deaths'].sum(),
            "Total Damage ('000 US$)": data['Total Damage (\'000 US$)'].sum()
        }
    else:
        return "No disaster data available for the specified country and year."

# Function to run Llama via Ollama
def run_llama_with_ollama(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2"],
            input=prompt,
            text=True,
            capture_output=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred: {e}"

# Initialize session state for conversation history
if "history" not in st.session_state:
    st.session_state["history"] = []
if "question_counter" not in st.session_state:
    st.session_state["question_counter"] = 0

# Display conversation history and input fields
for i, entry in enumerate(st.session_state["history"]):
    st.write(f"### Question {i+1}")
    st.write(entry["question"])
    st.write("### Answer")
    st.write(entry["answer"])

# Input area for a new question
user_question = st.text_input("## Ask your climate-related question:", key=f"user_input_{st.session_state['question_counter']}")
submit_button = st.button("Submit")

if submit_button and user_question.strip():
    answer = ""
    extracted_data = None

    # Check for small talk
    if is_small_talk(user_question):
        answer = "Hello! I'm here to assist with your climate and energy questions. Feel free to ask!"
    else:
        country, year, data_type = extract_info_from_text(user_question)

        if country and year:
            if data_type == "renewable":
                extracted_data = get_renewable_data(country, year)
                summary = generate_energy_summary(country, year)
                if extracted_data:
                    answer = f"Renewable energy data for {country} in {year}:\n{extracted_data}\n\nSummary:\n{summary}"
                else:
                    answer = "No renewable energy data found for the specified conditions."
            elif data_type == "disaster":
                extracted_data = get_disaster_data(country, year)
                summary = generate_disaster_summary(country, year)
                if extracted_data:
                    answer = f"Disaster data for {country} in {year}:\n{extracted_data}\n\nSummary:\n{summary}"
                else:
                    answer = "No disaster data found for the specified conditions."
            else:
                answer = "Specify whether you're interested in renewable energy or disaster data."

        else:
            answer = "Ensure to include the country and year in your query."

        # Generate a response using Llama if needed
        if extracted_data is None:
            llama_response = run_llama_with_ollama(user_question)
            answer += f"\n\nLlama's Response:\n{llama_response}"

    st.session_state["history"].append({
        "question": user_question,
        "answer": answer,
        "data": extracted_data
    })
    st.session_state["question_counter"] += 1


