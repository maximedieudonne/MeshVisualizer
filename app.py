import dash
import argparse
from layout import create_layout
from callbacks import register_callbacks

# Fonction principale pour exécuter l'application
def run_dash_app(mesh_path, texture_path=None):
    # Créer l'application Dash
    app = dash.Dash(__name__)

    # Ajouter le layout
    app.layout = create_layout(mesh_path, texture_path)

    # Enregistrer les callbacks
    register_callbacks(app, mesh_path, texture_path)

    # Lancer l'application
    app.run_server(debug=True)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Lancer l'application Dash pour visualiser un maillage 3D.")
    parser.add_argument('mesh_path', type=str, help="Chemin vers le fichier maillage .gii")
    parser.add_argument('--texture', type=str, help="Chemin vers le fichier texture .gii", default=None)
    args = parser.parse_args()

    # Lancer l'application avec les chemins fournis
    run_dash_app(args.mesh_path, args.texture)
