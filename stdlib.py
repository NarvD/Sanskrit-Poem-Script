# Import the functions from separate files
from .functions.vani import vani
from .functions.sankhya import sankhya
from .functions.lakara import lakara
from .functions.purusha import purusha
from .functions.vacana import vacana
from .functions.kriya import kriya
from .functions.kala import kala
from .functions.tithi import tithi
from .functions.ayana import ayana
from .functions.nakshatra import nakshatra
from .functions.yoga import yoga

class SanskritPoemScriptStdlib:
    def __init__(self):
        self._global_environment = {
            'vani': vani,
            'sankhya': sankhya,
            'lakara': lakara,
            'purusha': purusha,
            'vacana': vacana,
            'kriya': kriya,
            'kala': kala,
            'tithi': tithi,
            'ayana': ayana,
            'nakshatra': nakshatra,
            'yoga': yoga
            # Add more functions and variables to the global environment here.
        }

    def get_global_environment(self):
        return self._global_environment.copy()
