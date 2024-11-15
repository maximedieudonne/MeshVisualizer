import plotly.colors as pc
import numpy as np


# Fonction pour obtenir les noms des colormaps disponibles dans Plotly, en filtrant celles contenant '__' ou 'swatches'
def get_colorscale_names(colormap_type):
    if colormap_type == 'sequential':
        return [name for name in pc.sequential.__dict__.keys() if '__' not in name and 'swatches' not in name]
    elif colormap_type == 'diverging':
        return [name for name in pc.diverging.__dict__.keys() if '__' not in name and 'swatches' not in name]
    elif colormap_type == 'cyclical':
        return [name for name in pc.cyclical.__dict__.keys() if '__' not in name and 'swatches' not in name]
    return []


# Fonction pour convertir des couleurs RGB en hexadécimal
def convert_rgb_to_hex_if_needed(colormap):
    hex_colormap = []
    for color in colormap:
        if color.startswith('rgb'):
            rgb_values = [int(c) for c in color[4:-1].split(',')]
            hex_color = '#{:02x}{:02x}{:02x}'.format(*rgb_values)
            hex_colormap.append(hex_color)
        else:
            hex_colormap.append(color)
    return hex_colormap


# Création d'une colormap avec des traits noirs
def create_colormap_with_black_stripes(base_colormap, num_intervals=10, black_line_width=0.01):
    temp_c = pc.get_colorscale(base_colormap)
    temp_c_2 = [ii[1] for ii in temp_c]
    old_colormap = convert_rgb_to_hex_if_needed(temp_c_2)
    custom_colormap = []
    base_intervals = np.linspace(0, 1, len(old_colormap))

    num_intervals = len(old_colormap)
    for i in range(len(old_colormap) - 1):
        custom_colormap.append([base_intervals[i], old_colormap[i]])
        if i % (len(old_colormap) // num_intervals) == 0:
            black_start = base_intervals[i]
            black_end = min(black_start + black_line_width, 1)
            custom_colormap.append([black_start, 'rgb(0, 0, 0)'])
            custom_colormap.append([black_end, old_colormap[i]])
    custom_colormap.append([1, old_colormap[-1]])
    return custom_colormap


# fonction pour discretiser la colormap
def discretize_colormap(colormap, num_colors=10):
    colors = pc.get_colorscale(colormap)
    discrete_colors = []
    for i in range(num_colors):
        fraction = i / (num_colors - 1)
        color = pc.sample_colorscale(colors, fraction)[0]  # Extraire la couleur de la liste imbriquée
        discrete_colors.append([fraction, color])  # Ajouter le fractionnement et la couleur
    return discrete_colors


