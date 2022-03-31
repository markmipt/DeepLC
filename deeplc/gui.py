"""Graphical user interface."""
from multiprocessing import freeze_support
from pathlib import Path
import importlib.resources

from gooey import Gooey, local_resource_path

import deeplc.package_data.gui_images as img_module
from deeplc.__main__ import main


# Get path to package_data/images
# Workaround with parent of specific file required for Python 3.9+ support
with importlib.resources.path(img_module, 'config_icon.png') as resource:
    _IMG_DIR = Path(resource).parent


@Gooey(
    program_name="DeepLC",
    image_dir=local_resource_path(_IMG_DIR),
    tabbed_groups=True,
    default_size=(720, 480),
    monospace_display=True,
)
def start_gui():
    """Run main with GUI enabled."""
    main(gui=True)

if __name__ == "__main__":
    freeze_support()  # Required for multiprocessing with PyInstaller
    start_gui()
