import numpy as np


def set_initial_cond(temp_1d: np.ndarray, init_cond: np.ndarray | float) -> None:
    """
    :param temp_1d: Vecteur temperature pour conduction 1D
    :param init_cond: Conditions initiales sur la barre, hors conditions aux limites
    :return: Mets les conditions initiales au vecteur temperature
    """
    temp_1d[1:-1] = init_cond


def set_boundary_cond(temp_1d: np.ndarray, bound_cond_left: float, bound_cond_right: float) -> None:
    """
    :param temp_1d: Vecteur temperature pour conduction 1D
    :param bound_cond_left: Condition limite a gauche, x = 0
    :param bound_cond_right: Condition limite a droite, x = L
    :return: Mets les conditions limites au vecteur temperature
    """
    temp_1d[0] = bound_cond_left
    temp_1d[-1] = bound_cond_right


def initialize_temp(size: int,
                    init_cond: np.ndarray | float,
                    bound_conds_left: float,
                    bound_cond_right: float) -> np.ndarray:
    """
    :param size: Taille du vecteur temperature 1D
    :param init_cond: Conditions initiales
    :param bound_conds_left: Condition limite a gauche, x = 0
    :param bound_cond_right: Condition limite a droite, x = L
    :return: Cree le vecteur temperature 1D initial, a t = 0
    """
    temp_1d: np.ndarray = np.zeros((size, 1), dtype=float)
    set_initial_cond(temp_1d, init_cond)
    set_boundary_cond(temp_1d, bound_conds_left, bound_cond_right)
    return temp_1d


def create_conduction_mat(length_step: float, time_step: float, temp_1d_size: int) -> np.ndarray:
    """
    :param length_step: Pas de longueur
    :param time_step: Pas de temps
    :param temp_1d_size: Longueur du vecteur temperature 1D
    :return: Cree la matrice de conduction
    """
    # Lambda
    lbd: float = time_step / length_step ** 2

    # Matrice de conduction
    mat_subdiag: np.ndarray = np.diag((temp_1d_size - 1) * [- lbd], k=-1)
    mat: np.ndarray = np.diag(temp_1d_size * [1 + 2 * lbd]) + mat_subdiag + mat_subdiag.T
    return mat


def compute_new_temp(temp_1d: np.ndarray, mat: np.ndarray) -> np.ndarray:
    """
    :param temp_1d: Vecteur temperature pour conduction 1D a l'instant t
    :param mat: Matrice de conduction 1D
    :return: Renvoie la temperature 1D a l'instant t + 1
    """
    return np.linalg.inv(mat) @ temp_1d
