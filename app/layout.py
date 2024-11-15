from dash import  html, dcc
import dash_bootstrap_components as dbc  # Pour utiliser les composants de style Bootstrap



# Liste de 10 couleurs prédéfinies
COLOR_OPTIONS = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"
]

def create_layout():
    return html.Div([
        # Titre
        html.Div(
            html.H1(
                "Mesh Visualizer", 
                style={
                    'textAlign': 'center', 
                    'color': '#2c3e50',
                    'fontFamily': 'Arial, sans-serif',
                    'fontWeight': 'bold',
                    'fontSize': '36px',
                    'margin': '20px 0'
                }
            ), 
            style={'width': '100%'}
        ),

        # Interface principale
        html.Div([
            # Bande gauche (listes de div)
            html.Div([
                html.Label("Sélectionner le type de colormap"),
                dcc.Dropdown(
                    id='colormap-type-dropdown',
                    options=[
                        {'label': 'Sequential', 'value': 'sequential'},
                        {'label': 'Diverging', 'value': 'diverging'},
                        {'label': 'Cyclical', 'value': 'cyclical'}
                    ],
                    value='sequential',
                    clearable=False
                ),
                html.Label("Sélectionner une colormap"),
                dcc.Dropdown(
                    id='colormap-dropdown',
                    value='Viridis',
                    clearable=False
                ),
                html.Button(
                    "Personnaliser ma colormap",
                    id='custom-colormap-button',
                    n_clicks=0,
                    style={'margin-top': '20px'}
                ),

                html.Div([
                    html.Label("Discrétiser la colormap"),
                    dcc.Checklist(
                        id='toggle-discrete-colormap', 
                        options=[{'label': 'Oui', 'value': 'on'}], 
                        value=[], 
                        inline=True
                    ),
                    html.Label("Afficher les isolignes"),
                    dcc.Checklist(
                        id='toggle-contours', 
                        options=[{'label': 'Oui', 'value': 'on'}], 
                        value=[], 
                        inline=True
                    ),
                    html.Label("Activer traits noirs"),
                    dcc.Checklist(
                        id='toggle-black-intervals', 
                        options=[{'label': 'Oui', 'value': 'on'}], 
                        value=[], 
                        inline=True
                    ),
                    html.Label("Centrer la colormap sur 0"),
                    dcc.Checklist(
                        id='toggle-center-colormap', 
                        options=[{'label': 'Oui', 'value': 'on'}], 
                        value=[], 
                        inline=True
                    )
                ])


            ], style={
                'width': '300px',
                'padding': '20px',
                'border': '2px solid #2c3e50',
                'borderRadius': '10px',
                'backgroundColor': '#f9f9f9'
            }),

            # Graphe central
            html.Div([
                dcc.Graph(id='3d-mesh')
            ], style={
                'flex': '1',
                'padding': '20px',
                'border': '2px solid #2c3e50',
                'borderRadius': '10px',
                'backgroundColor': '#ffffff'
            }),

            # Bande droite (slider)
            html.Div([
                dcc.RangeSlider(
                    id='range-slider',
                    min=0,
                    max=1,
                    step=0.01,
                    value=[0, 1],
                    marks={i: str(i) for i in range(0, 11)},
                    vertical=True
                )
            ], style={
                'width': '100px',
                'padding': '20px',
                'border': '2px solid #2c3e50',
                'borderRadius': '10px',
                'backgroundColor': '#f9f9f9'
            })
        ], style={
            'display': 'flex',
            'justifyContent': 'space-between',
            'alignItems': 'flex-start'
        }),

        # Modale pour personnalisation de la colormap
        dbc.Modal([
            dbc.ModalHeader("Personnaliser la colormap"),
            dbc.ModalBody([
                html.Div("Colormap actuelle :"),
                html.Div(id='current-colorbar', style={
                    'height': '40px',
                    'width': '100%',
                    'background': 'linear-gradient(to right, #1f77b4, #1f77b4)',
                    'marginBottom': '20px'
                }),
                html.Div("Sélectionner une nouvelle couleur :", style={'marginBottom': '10px'}),
                html.Div([
                    html.Div(
                        style={
                            'backgroundColor': color,
                            'height': '40px',
                            'width': '40px',
                            'display': 'inline-block',
                            'margin': '5px',
                            'cursor': 'pointer',
                            'border': '1px solid black'
                        },
                        id={'type': 'color-square', 'index': i}
                    ) for i, color in enumerate(COLOR_OPTIONS)
                ], style={'display': 'flex', 'flexWrap': 'wrap', 'marginBottom': '20px'}),
                html.Div([
                    html.Label("Valeur min :"),
                    dcc.Input(id='color-min', type='number', value=0, style={'marginRight': '10px'}),
                    html.Label("Valeur max :"),
                    dcc.Input(id='color-max', type='number', value=10)
                ], style={'marginBottom': '20px'}),
                html.Button("Ajouter une couleur", id='add-color-button', n_clicks=0),
                html.Button("Créer la colormap", id='create-colormap-button', n_clicks=0, style={'marginLeft': '10px'})
            ]),
            dbc.ModalFooter(
                html.Button("Fermer", id='close-modal-button', n_clicks=0)
            )
        ], id='color-modal', is_open=False)
    ])