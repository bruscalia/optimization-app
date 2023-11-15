import os
from io import BytesIO
from typing import Any

import streamlit as st

# from optimize.dataloader import
from optimize.model import solve_model
# from optimize.writer import


# Define mime for input and output
INPUT_TYPE = "json"
OUTPUT_TYPE = "json"


# Create current solution as session_state
if "input_data" not in st.session_state:
    st.session_state.input_data = None

if "output" not in st.session_state:
    st.session_state.output = None


# Callback uploading a new file
def upload_callback():
    st.session_state.input_data = None
    st.session_state.output = None


# TODO: Define a function to write output file
@st.cache
def write_output_file(output: Any) -> BytesIO:
    buffer = BytesIO()
    # Write your output writing function
    # Some standard options are available at `optimize.writer`
    buffer.seek(0)
    return buffer


# TODO: Define a function to read input file
@st.cache
def read_input_file(buffer: BytesIO) -> Any:
    # Write your input reading function
    # Some standard options are available at `optimize.dataloader`
    data = None
    # data = ...
    return data


# Path to icon
icon_path = os.path.join("assets", "icon_tsp.png")

# Set the page config to wide mode
st.set_page_config(
    page_title="Optimization App",
    page_icon=icon_path,
    layout="wide",
)

st.sidebar.image(icon_path)

st.title("Optimization App")
st.write("Welcome to the Optimization App.")

# Here you load the input file
file = st.file_uploader("Upload input file", type=[f"{INPUT_TYPE}"], on_change=upload_callback)

# Pass this or other parameters to your solve model function
time_limit = st.sidebar.number_input("Time limit", min_value=0, value=5, step=1)

# Start when file is ready
if file is not None:
    input_data = read_input_file(file)
    st.session_state.input_data = input_data
    start_button = st.button("Optimize")

    # Run if start is pressed
    if file is not None and start_button:

        # Create a spinner while solving
        with st.spinner("Optimizing"):

            # Solve model
            output = solve_model(st.session_state.input_data)
            st.session_state.output = output

# Download output
if st.session_state.output is not None:
    output_file = write_output_file(st.session_state.output)
    st.download_button(
        label="Download Output",
        data=output_file,
        file_name=f"output.{OUTPUT_TYPE}",
        mime=OUTPUT_TYPE,
    )

# Additional display
# TODO: your additional features for analytics
