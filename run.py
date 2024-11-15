import argparse
from app import dash_app

# Fonction d'entrée pour gérer les arguments de la ligne de commande
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Launch the Dash application for 3D mesh visualization.")
    parser.add_argument('mesh_path', type=str, help="Path to the .gii mesh file")
    parser.add_argument('--texture', type=str, help="Path to the .gii texture file", default=None)
    args = parser.parse_args()

    # Launch the Dash application with the provided paths
    dash_app.create_dash_app(args.mesh_path, args.texture).run_server(debug=True)
