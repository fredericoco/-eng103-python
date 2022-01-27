# import random
# from functions.os_functions import return_user_id
# from my_classes.game_class import game


from random import random, randint
from math import pi, ceil, floor
import numpy as np

import functions.os_functions

# work_dir = os.getcwd()
# print(work_dir)
# print(np.pi)
#
# print(random())
# print(pi)
# print(ceil(pi))
# print(floor(pi))
#
# print(randint(0, 100))


# print(return_user_id())
#
# a=game("NV","PC",100)
# print(a.name)

# PIP -> PIP Installs Packages (Auto-acronym)
import requests

r = requests.get("http://www.bbc.co.uk")
print(r, type(r))
print(r.status_code)
# print(r.content)
