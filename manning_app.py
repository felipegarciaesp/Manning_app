# Codigo para calcular altura normal y altura critica en canales (escurrimiento libre)

## Importar librerias ##
from scipy.optimize import fsolve
import numpy as np

## Definicion valores globales ##
g = 9.81    # aceleracion de la gravedad (m/s^2)

## Definicion de funciones ##
def manning_eq(h):
    A = b * h           # area de escurrimiento - canal rectangular (m^2)
    Pm = b + 2 * h      # perimetro mojado - canal rectangular (m)
    Rh = A / Pm         # radio hidráulico (m)
    f = ((np.sqrt(S)/n) * A * (Rh ** (2/3)) - Q) * 1000000    # funcion que debe ser igual a 0.
    return float(f[0]) #Se extrae escalar para evitar warnings

def h_critica(h):
    A = b * h           # area de escurrimiento - canal rectangular (m^2).
    V = Q / A           # velocidad de escurrimiento (m/s).
    T = b               # ancho superficial de escurrimiento - canal rectangular (m)
    f = (froude(V, A, T) - 1) * 1000000
    return float(f[0]) #Se extrae escalar para evitar warnings

def froude(V, A, T):                # funcion para calcular el numero de froude en una seccion.
    # V: velocidad [m/s]
    # A: área [m^2]
    # T: tirante [m]
    # g: aceleración de la gravedad [m/s^2]
    return V / np.sqrt(g * A / T)

## Datos del problema ##
b = 3.0      # ancho del canal rectangular (m)
Q = 10.0     # caudal (m^3/s)
S = 0.001    # pendiente del canal (m/m)
n = 0.03     # coeficiente de Manning (adim.)

# Valor inicial para la altura
h0 = b / 2              # valor inicial para canal rectangular

# Resolver la ecuación
altura_normal = fsolve(manning_eq, h0)[0]
altura_critica = fsolve(h_critica, h0)[0]
print(f"Altura normal: {altura_normal:.3f} m")
print(f"Altura critica: {altura_critica:.3f} m")