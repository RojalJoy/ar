import streamlit as st

st.title('AR Character Viewer')
st.write('This app loads and displays AR characters.')

# Placeholder for AR character (a box in this case)
import open3d as o3d
import numpy as np

# Create a box
mesh_box = o3d.geometry.TriangleMesh.create_box()

# Convert to streamlit
st.write(mesh_box)
