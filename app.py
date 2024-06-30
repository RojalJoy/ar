import streamlit as st
import pythreejs as p3js
import numpy as np

st.title('AR Character Viewer')
st.write('This app loads and displays AR characters.')

# Create a simple 3D box using pythreejs
box_geometry = p3js.BoxBufferGeometry()
material = p3js.MeshStandardMaterial(color='red')
box = p3js.Mesh(geometry=box_geometry, material=material)

# Set up the scene, camera, and renderer
camera = p3js.PerspectiveCamera(position=[3, 3, 3], fov=20)
scene = p3js.Scene(children=[box, p3js.AmbientLight(color='white', intensity=0.8)])
renderer = p3js.Renderer(camera=camera, scene=scene, controls=[p3js.OrbitControls(controlling=camera)], width=600, height=400)

# Render the scene in Streamlit
st.write(renderer)
