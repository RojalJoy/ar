import streamlit as st
import pythreejs as p3js
from IPython.display import display
import ipywidgets as widgets
import streamlit.components.v1 as components
from nbconvert import HTMLExporter
import nbformat

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

# Function to convert widget to HTML using nbconvert
def render_widget(widget):
    # Create a notebook with the widget
    notebook = nbformat.v4.new_notebook()
    notebook.cells.append(nbformat.v4.new_code_cell("from IPython.display import display\n" + "import pythreejs as p3js\n" + "display(widget)"))
    notebook.cells[0].outputs = [{"output_type": "display_data", "data": widget._repr_mimebundle_(), "metadata": {}}]

    # Convert the notebook to HTML
    html_exporter = HTMLExporter()
    (body, resources) = html_exporter.from_notebook_node(notebook)
    return body

# Get the HTML representation of the renderer widget
widget_html = render_widget(renderer)

# Display the HTML in Streamlit
components.html(widget_html, height=600)

st.write("Rendered 3D Box")
