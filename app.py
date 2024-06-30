import streamlit as st
import streamlit.components.v1 as components

# Import AR.js library
ar_js_script = """
<script src="https://cdn.jsdelivr.net/npm/ar.js@1.9.3/aframe.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/ar.js@1.9.3/ar.js"></script>
"""

components.html(ar_js_script)

st.title('AR Character Viewer')

# Replace with your 3D model URL or data
model_url = "path/to/your/ar_model.glb"

ar_scene = """
<a-scene arjs>
    <a-marker preset="hiro">
        <a-entity gltf-model="#model" rotation="0 180 0"></a-entity>
    </a-marker>
    <a-entity id="model" gltf-model="{model_url}"></a-entity>
</a-scene>
""".format(model_url=model_url)

components.html(ar_scene, height=600)
