import streamlit as st
import streamlit.components.v1 as components

st.title('AR Character Viewer')
st.write('This app loads and displays AR characters.')

# Three.js code to create and render a 3D box in AR
three_js_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; }
        canvas { display: block; }
    </style>
</head>
<body>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
    <script>
        // Check for WebXR support
        if (navigator.xr) {
            navigator.xr.isSessionSupported('immersive-ar').then(function (supported) {
                if (supported) {
                    // Setup Three.js scene
                    var scene = new THREE.Scene();
                    var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                    var renderer = new THREE.WebGLRenderer({ alpha: true });
                    renderer.setSize(window.innerWidth, window.innerHeight);
                    renderer.xr.enabled = true;
                    document.body.appendChild(renderer.domElement);

                    // Create a box
                    var geometry = new THREE.BoxGeometry(0.1, 0.1, 0.1);
                    var material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
                    var cube = new THREE.Mesh(geometry, material);
                    scene.add(cube);

                    // Setup WebXR
                    navigator.xr.requestSession('immersive-ar', {
                        requiredFeatures: ['local-floor'],
                        optionalFeatures: ['bounded-floor']
                    }).then(function (session) {
                        renderer.xr.setSession(session);

                        var controller = renderer.xr.getController(0);
                        scene.add(controller);

                        session.requestAnimationFrame(function animate() {
                            session.requestAnimationFrame(animate);
                            renderer.render(scene, camera);
                        });

                        controller.addEventListener('select', function () {
                            cube.position.set(0, 0, -0.5).applyMatrix4(controller.matrixWorld);
                            cube.visible = !cube.visible;
                        });
                    });
                } else {
                    document.body.innerHTML = '<h1>WebXR not supported</h1>';
                }
            });
        } else {
            document.body.innerHTML = '<h1>WebXR not supported</h1>';
        }
    </script>
</body>
</html>
"""

# Display the HTML content in Streamlit
components.html(three_js_code, height=600)

st.write("Rendered 3D Model in AR")
