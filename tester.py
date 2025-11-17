import streamlit as st
import requests
from env_vars import * # Assuming this contains your SERVER_ info

# ... other setup ...

agents = []  # Initialize agents as an empty list

try:
    # 1. Make the request to the FastAPI server's /agents endpoint
    resp = requests.get(f"{SERVER_HTTP_SCHEME}://{SERVER_ADDR}:{SERVER_PORT}/agents")
    
    # 2. Check the response status code
    if resp.status_code == 200:
        agents = resp.json()  # Assign the list if successful
    else:
        # If server responded but with an error status (e.g., 404, 500)
        st.error(f"Failed to fetch agents. Server responded with status code: {resp.status_code}")
        
except requests.exceptions.ConnectionError:
    # If the server is not running or connection is refused
    st.error(f"Connection Error: Could not connect to the server at {SERVER_ADDR}:{SERVER_PORT}. Please ensure the server is running.")
except Exception as e:
    # Catch any other potential errors
    st.error(f"An unexpected error occurred while fetching agents: {e}")

# This line is now safe because 'agents' is guaranteed to be a list ([] if any failure occurred)
st.subheader(f"Agent Count: {len(agents)}")