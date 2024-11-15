# MeshVisualizer

**MeshVisualizer** is an interactive 3D mesh visualization tool designed for exploring and analyzing scalar fields mapped onto mesh structures. The tool allows users to load mesh files, apply colormaps, and visualize scalar data in an intuitive, customizable interface. It supports various colormap types (sequential, diverging, cyclical) and offers features like discrete color intervals, contour visualization, and black stripes for enhanced readability.

## Features

- **3D Mesh Visualization**: Display 3D meshes with scalar data applied to their vertices.
- **Customizable Colormaps**: Choose from a variety of predefined colormaps or create custom colormaps with black intervals and discrete color steps.
- **Contour Lines**: Optionally display isolines on the mesh for better data interpretation.
- **Interactive Controls**: Use sliders, checklists, and dropdowns to interactively adjust colormap ranges, view scalar values, and toggle visualization settings.
- **File Support**: Load mesh data from `.gii` files, which is commonly used in neuroimaging and computational neuroscience.
- **Cross-platform**: Built with Dash and Plotly, ensuring smooth performance on any modern web browser.

## Installation

To install the required dependencies, clone the repository and install the necessary Python packages.

```bash
git clone https://github.com/yourusername/MeshVisualizer.git
cd MeshVisualizer
pip install -r requirements.txt
```

## Usage

Run the app by specifying the path to your mesh file and optionally a texture file for scalar data:

```bash
python app.py <path_to_mesh_file> --texture <path_to_texture_file>
```

Once the app is running, you can interact with the 3D mesh visualization, adjust visualization parameters, and explore your data in an interactive environment.

## Contributing

Feel free to fork the project, submit issues, and open pull requests. We welcome contributions to improve the functionality and user experience!

