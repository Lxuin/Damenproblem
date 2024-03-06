def damen_zu_dimacs(N):
    klauseln = []

    def var(i, j):
        # funktion zur erzeugung einer eindeutigen Variablen für die Position (i, j)
        return i * N + j + 1

    # min 1 dame in reihe
    for i in range(N):
        klauseln.append([var(i, j) for j in range(N)])

    # min 1 dame in spalte
    for j in range(N):
        klauseln.append([var(i, j) for i in range(N)])

    #  max 1 dame in reihe
    for i in range(N):
        for j in range(N):
            for k in range(j + 1, N):
                klauseln.append([-var(i, j), -var(i, k)])

    #  max 1 dame in spalte
    for j in range(N):
        for i in range(N):
            for k in range(i + 1, N):
                klauseln.append([-var(i, j), -var(k, j)])

    # keine zwei damen in derselben diagonalen
    for i in range(N):
        for j in range(N):
            for k in range(1, N):
                if i + k < N and j + k < N:
                    klauseln.append([-var(i, j), -var(i + k, j + k)])
                if i + k < N and j - k >= 0:
                    klauseln.append([-var(i, j), -var(i + k, j - k)])

    # convert zu DIMACS-Format
    dimacs = f"p cnf {N * N} {len(klauseln)}\n"
    dimacs += "\n".join(" ".join(map(str, clause)) + " 0" for clause in klauseln)
    return dimacs

# Beispiel für n
n = 5
beispiel = damen_zu_dimacs(n)
print(beispiel)

# Speichert es als File
with open(f"damenproblem_dimacs_N{n}.cnf", "w") as file:
    file.write(beispiel)
