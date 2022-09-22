__author__ = 'aymgal'

from typing import Tuple

from coolest.template.api.profile_list import ProfileList
from coolest.template.api.profiles import mass as mass_profiles_module
from coolest.template.api.profiles import light as light_profiles_module


class MassModel(ProfileList):

    def __init__(self, 
                 *profile_names: Tuple[str]) -> None:
        super().__init__(mass_profiles_module, *profile_names)
        

class LightModel(ProfileList):

    def __init__(self, 
                 *profile_names: Tuple[str]) -> None:
        super().__init__(light_profiles_module, *profile_names)