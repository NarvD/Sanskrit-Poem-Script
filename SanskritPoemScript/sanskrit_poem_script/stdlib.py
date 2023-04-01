# Import the functions from separate files
from .functions.vani import vani
from .functions.sankhya import sankhya
# Import more functions here as needed.

class SanskritPoemScriptStdlib:
    def __init__(self):
        self._global_environment = {
            'vani': vani,
            'sankhya': sankhya,
            # Add more functions and variables to the global environment here.
        }

    def get_global_environment(self):
        return self._global_environment.copy()

