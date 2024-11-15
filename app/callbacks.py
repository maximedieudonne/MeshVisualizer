from dash.dependencies import Input, Output, State, ALL
from dash import callback_context
from app import plot

# Liste des couleurs initiales
DEFAULT_COLOR = "#1f77b4"  # Bleu par défaut pour la colormap
CUSTOM_COLORMAPS = {}  # Dictionnaire pour stocker les colormaps personnalisées


def register_callbacks(app, vertices, faces, scalars):
    """
    Enregistre les callbacks nécessaires à l'application Dash.
    """
    # Callback pour mettre à jour le graphe 3D
    @app.callback(
        Output('3d-mesh', 'figure'),
        [
            Input('range-slider', 'value'),
            Input('toggle-contours', 'value'),
            Input('toggle-black-intervals', 'value'),
            Input('colormap-dropdown', 'value'),
            Input('toggle-center-colormap', 'value'),
            Input('toggle-discrete-colormap', 'value')
        ],
        [State('3d-mesh', 'relayoutData')]
    )
    def update_figure(value_range, toggle_contours, toggle_black_intervals, selected_colormap, center_colormap, discrete_colormap, relayout_data):
        """
        Met à jour le graphe 3D en fonction des paramètres choisis par l'utilisateur.
        """
        min_value, max_value = value_range
        camera = relayout_data['scene.camera'] if relayout_data and 'scene.camera' in relayout_data else None
        show_contours = 'on' in toggle_contours
        use_black_intervals = 'on' in toggle_black_intervals
        center_on_zero = 'on' in center_colormap

        fig = plot.plot_mesh_with_colorbar(
            vertices, faces, scalars, 
            color_min=min_value, color_max=max_value,
            camera=camera, show_contours=show_contours, 
            colormap=selected_colormap,
            use_black_intervals=use_black_intervals, 
            center_colormap_on_zero=center_on_zero
        )
        return fig

    # Callback pour mettre à jour les options de colormap
    @app.callback(
        Output('colormap-dropdown', 'options'),
        Input('colormap-type-dropdown', 'value')
    )
    def update_colormap_options(selected_type):
        """
        Met à jour les options de colormap disponibles en fonction du type choisi.
        """
        from utils.colormap_utils import get_colorscale_names
        options = [{'label': cmap, 'value': cmap} for cmap in get_colorscale_names(selected_type)]
        # Ajouter les colormaps personnalisées
        if CUSTOM_COLORMAPS:
            options.append({'label': '--- Personnalisées ---', 'value': ''})
            options.extend([{'label': name, 'value': name} for name in CUSTOM_COLORMAPS.keys()])
        return options

    # Callback pour gérer l'ouverture et la fermeture de la fenêtre modale
    @app.callback(
        Output('color-modal', 'is_open'),
        [Input('custom-colormap-button', 'n_clicks'),
         Input('close-modal-button', 'n_clicks')],
        [State('color-modal', 'is_open')]
    )
    def toggle_modal(custom_clicks, close_clicks, is_open):
        """
        Affiche ou masque la fenêtre modale en fonction des clics sur les boutons.
        """
        ctx = callback_context
        if not ctx.triggered:
            return is_open
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id in ['custom-colormap-button', 'close-modal-button']:
            return not is_open
        return is_open

    # Callback pour mettre à jour la colorbar actuelle
    @app.callback(
        Output('current-colorbar', 'style'),
        Output('color-preview', 'children'),
        Input('add-color-button', 'n_clicks'),
        State({'type': 'color-square', 'index': ALL}, 'style'),
        State('color-min', 'value'),
        State('color-max', 'value'),
        State('current-colorbar', 'style')
    )
    def update_colorbar(n_clicks, colors, min_value, max_value, current_style):
        """
        Met à jour la colormap en fonction des paramètres définis par l'utilisateur.
        """
        if n_clicks is None or min_value is None or max_value is None:
            return current_style, "Colormap par défaut"
        
        selected_color = None
        for color in colors:
            if color.get('border') == '3px solid black':  # Couleur sélectionnée
                selected_color = color['backgroundColor']
                break

        if not selected_color:
            return current_style, "Sélectionnez une couleur"

        # Ajouter une nouvelle bande colorée à la colormap
        gradient = current_style.get('background', f'linear-gradient(to right, {DEFAULT_COLOR}, {DEFAULT_COLOR})')
        gradient_parts = gradient.replace('linear-gradient(to right, ', '').rstrip(')').split(', ')
        new_gradient = gradient_parts + [selected_color] * (max_value - min_value)
        new_style = {
            'height': '40px',
            'width': '100%',
            'background': f'linear-gradient(to right, {", ".join(new_gradient)})'
        }
        return new_style, f"Couleur ajoutée : {selected_color}, Min : {min_value}, Max : {max_value}"

    # Callback pour finaliser et enregistrer la colormap
    @app.callback(
        Output('colormap-dropdown', 'value'),
        Input('create-colormap-button', 'n_clicks'),
        State('current-colorbar', 'style'),
        State('colorbar-name', 'value')
    )
    def create_colormap(n_clicks, colorbar_style, colormap_name):
        """
        Crée une nouvelle colormap personnalisée et l'ajoute aux options disponibles.
        """
        if n_clicks is None or not colormap_name:
            return dash.no_update
        CUSTOM_COLORMAPS[colormap_name] = colorbar_style['background']
        return colormap_name
