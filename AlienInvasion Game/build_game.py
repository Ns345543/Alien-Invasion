import PyInstaller.__main__
import os

# Define the base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Define paths to assets
images_path = os.path.join(base_path, 'images')
sfx_path = os.path.join(base_path, 'Sfx')

# Separator for add-data (semicolon for Windows, colon for Unix)
separator = ';' if os.name == 'nt' else ':'

PyInstaller.__main__.run([
    'Alien_invasion.py',
    '--onefile',
    '--noconsole',
    '--name=AlienInvasion',
    f'--add-data={images_path}{separator}images',
    f'--add-data={sfx_path}{separator}Sfx',
    '--clean',
])
