import numpy as np

# Longueur
L = 1
h = 0.01
x = np.arange(0, L + h, h)
nx = len(x)

# Temps
k = 0.0001

# Conditions limites en x = 0 et x = L
T_x0 = 0
T_xL = 0

# Conditions initiales a t = 0
T_x = 0
