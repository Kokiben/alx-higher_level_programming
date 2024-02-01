#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard.
Program that solves the N queens problem.
"""


from sys import argv

if __name__ == "__main__":
    b = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for l in range(n):
        b.append([l, None])

    def already_exists(u):
        """check that b queen does not already exist in that u value"""
        for w in range(n):
            if u == b[w][1]:
                return True
        return False

    def reject(w, u):
        """determines whether or not to reject the solution"""
        if (already_exists(u)):
            return False
        l = 0
        while (l < w):
            if abs(b[l][1] - u) == abs(l - w):
                return False
            l += 1
        return True

    def clear_b(w):
        """clears the answers from the point of failure on"""
        for l in range(w, n):
            b[l][1] = None

    def nqueens(w):
        """recursive backtracking function to find the solution"""
        for u in range(n):
            clear_b(w)
            if reject(w, u):
                b[w][1] = u
                if (w == n - 1):  # accepts the solution
                    print(b)
                else:
                    nqueens(w + 1)  # moves on to next w value to continue

    # w = 0
    nqueens(0)
