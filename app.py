import streamlit as st
from tuya_connector import TuyaOpenAPI, AuthType

# Tuya API credentials
ACCESS_ID = "your-access-id"
ACCESS_KEY = "your-access-key"
API_ENDPOINT = "https://openapi.tuyaus.com"  # Use the endpoint specific to your region
USERNAME = "your-email@example.com"
PASSWORD = "your-password"
DEVICE_ID = "your-device-id"

# Initialize Tuya OpenAPI
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY, AuthType.CUSTOM)
openapi.connect(USERNAME, PASSWORD)

st.title("Smart Life Device Controller")

# Button to turn on the device
if st.button("Turn On"):
    commands = {'commands': [{'code': 'switch_led', 'value': True}]}
    response = openapi.post(f'/v1.0/devices/{DEVICE_ID}/commands', commands)
    st.write("Turned On:", response)

# Button to turn off the device
if st.button("Turn Off"):
    commands = {'commands': [{'code': 'switch_led', 'value': False}]}
    response = openapi.post(f'/v1.0/devices/{DEVICE_ID}/commands', commands)
    st.write("Turned Off:", response)
