import random

def bron_kerbosch(G, P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    try:
        u = random.choice(list(P.union(X)))
        S = P.difference(G[u])
    # if union of P and X is empty
    except IndexError:
        S = P
    for v in S:
        yield from bron_kerbosch(G,
            P=P.intersection(G[v]), R=R.union([v]), X=X.intersection(G[v]))
        P.remove(v)
        X.add(v)

