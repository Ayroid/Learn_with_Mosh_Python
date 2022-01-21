# Modules are codes containing functions of similar types
# Modules are created to better organise a code or project
# They promote reusability of code & make the code easier to understand

import L46_Modules_2                # We are importing all the functions present in module L46_Modules_2.py
L46_Modules_2.hey()                 # When importing all functions we have to use a dot operator to call functions

from L46_Modules_2 import greet     # We are importing specific functions form L46_Modules_2.py
greet()                             # No need to use the dot operator when using this method