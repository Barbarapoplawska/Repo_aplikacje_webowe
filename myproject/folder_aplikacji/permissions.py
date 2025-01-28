import copy
from rest_framework import permissions

class CustomDjangoModelPermissions(permissions.DjangoModelPermissions):
    """
    Dodatkowa klasa uprawnień, która pozwala na sprawdzenie uprawnień w zależności od właściciela obiektu.
    """
    def __init__(self):
        selfperms_map = copy.deepcopy(self.perms_map)
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']
        self.perms_map['DELETE'] = ['%(app_label)s.view_%(model_name)s']

        



