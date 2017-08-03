
def c(n, r):
    if r == 1:
        return n
    if n == r:
        return n
    return c(n - 1, r) + c(n - 1, r - 1)
