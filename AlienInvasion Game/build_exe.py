import PyInstaller.__main__
import os
import shutil

# Define the base path
base_path = os.path.dirname(os.path.abspath(__file__))

# Define paths to assets
images_path = os.path.join(base_path, 'images')
sfx_path = os.path.join(base_path, 'Sfx')

# Separator for add-data (semicolon for Windows, colon for Unix)
separator = ';' if os.name == 'nt' else ':'

# Clean previous build
try:
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
except PermissionError:
    print("ERROR: Cannot delete build files. Please close Alien_invasion.exe if it's running.")
    print("Check Task Manager and end any Alien_invasion.exe processes, then try again.")
    input("Press Enter to exit...")
    exit(1)

print("Building Alien Invasion...")

PyInstaller.__main__.run([
    'Alien_invasion.py',
    '--onefile',
    '--noconsole',
    '--name=Alien_invasion',
    f'--add-data={images_path}{separator}images',
    f'--add-data={sfx_path}{separator}Sfx',
    '--clean',
])

print("Build complete! Executable is in the 'dist' folder.")
