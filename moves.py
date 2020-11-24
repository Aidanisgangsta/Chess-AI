import board

N = -8
E = 1
S = 8
W = -1

moves = {
    "p": (N, N+N, N+E, N+W),
    "r": (N, E, S, W),
    "n": (N+N+W, N+N+E, E+E+N, E+E+S, S+S+E, S+S+W, W+W+S, W+W+N),
    "b": (N+W, N+E, S+W, S+E),
    "q": (N, E, S, W, N+W, N+E, S+W, S+E),
    "k": (N, E, S, W, N+W, N+E, S+W, S+E)
}

def main():
    board.printboard()

if __name__ == '__main__':
    main()