import matplotlib.pyplot as plt

def zeichne_schachbrett(sat_output, N):

    schachbrett = [[0 for _ in range(N)] for _ in range(N)]

    # damen platzieren
    for num in sat_output:
        if num > 0:
            reihe = (num - 1) // N
            spalte = (num - 1) % N
            schachbrett[reihe][spalte] = 1

    fig, ax = plt.subplots()

    # schachbrett zeichene
    for i in range(N):
        for j in range(N):
            if schachbrett[i][j] == 1:
                ax.add_patch(plt.Rectangle((j, N-1-i), 1, 1, color="green"))
            else:
                ax.add_patch(plt.Rectangle((j, N-1-i), 1, 1, color="white" if (i+j)%2 == 0 else "gray"))


    ax.set_xlim([0, N])
    ax.set_ylim([0, N])
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

# bsp
sat_output = [-1, -2, -3, 4, -5, -6, -7, -8, -9, 10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, 23, -24, -25, -26, 27, -28, -29, -30, -31, -32, -33, -34, -35, -36, -37, 38, -39, -40, -41, -42, -43, -44, -45, -46, -47, 48, -49, -50, -51, -52, 53, -54, -55, -56, 57, -58, -59, -60, -61, -62, -63, -64]
#8x8
N = 8
zeichne_schachbrett(sat_output, N)
