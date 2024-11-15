import dash
from dash import dcc, html
import plotly.graph_objects as go
import numpy as np
from app import callbacks, layout, plot
from utils import rw as rw
from utils import colormap_utils as cu


# Fonction principale pour initialiser l'application Dash
def create_dash_app(mesh_path, texture_path=None):
    # Charger le mesh
    mesh = rw.load_mesh(mesh_path)
    vertices = mesh.vertices
    faces = mesh.faces

    # Charger la texture (si fournie)
    scalars = rw.read_gii_file(texture_path) if texture_path else None

    # Initialiser l'application Dash
    app = dash.Dash(__name__)

    # Définir le layout de l'application
    app.layout = layout.create_layout()

    # Enregistrer les callbacks
    callbacks.register_callbacks(app, vertices, faces, scalars)

    return app