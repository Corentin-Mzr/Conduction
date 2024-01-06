import matplotlib
import matplotlib.pyplot as plt
from conduction import create_conduction_mat, initialize_temp, compute_new_temp
from parameters import *

if __name__ == "__main__":
    # Affichage
    matplotlib.use("TkAgg")

    # Matrice de conduction
    M = create_conduction_mat(h, k, nx)

    # Vecteur temperature initial, a t = 0
    T = initialize_temp(nx, T_x, T_x0, T_xL)
    T[nx // 2:] = 10
    T_max = np.max(T)
    print(T_max)

    try:
        t = 0
        fig, ax = plt.subplots()
        data, = ax.plot(x, T)
        ax.axis([-0.1, L + 0.1, 0, 1.1 * np.max(T)])
        ax.set_xlabel('Position')
        ax.set_ylabel('Temperature')
        plt.title("Convection 1D")
        plt.show(block=False)
        while plt.fignum_exists(fig.number):
            T = compute_new_temp(T, M)
            data.set_ydata(T)
            data.set_color([np.max(T) / T_max if T_max else 0, 0, 1 - np.max(T) / T_max if T_max else 0])
            fig.canvas.draw_idle()
            fig.canvas.flush_events()
            ax.set_title(f'Convection 1D\nt={t:.5f}s')
            t += k
    except Exception as e:
        print(e)
    finally:
        plt.close()
