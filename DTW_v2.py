import numpy as np


def bestpath(df):
    path = []
    path.append((0, 0))
    l = len(df)

    i, j = 0, 0
    while i < l - 1 and j < l - 1:
        idx = np.argmin([df[i + 1, j + 1], df[i + 1, j], df[i, j + 1]])
        if idx == 0:
            i = i + 1
            j = j + 1
        elif idx == 1:
            i = i + 1
        elif idx == 2:
            j = j + 1
        path.append((i, j))

    while j < l - 1:
        j = j + 1
        path.append((i, j))
    while i < l - 1:
        i = i + 1
        path.append((i, j))

    return path


def Compute_comLen(df):
    v = []
    path = bestpath(df)
    length = 0
    for i in range(len(path)-1):
        if path[i + 1][0] == path[i][0] + 1 and path[i+1][1] == path[i][1] + 1:
            length = length +1
        else:
            v.append(length)
            length = 0
    v.append(length)
    return v


def compute_w(df):
    path = bestpath(df)
    seqLen = len(path)
    v = Compute_comLen(df)
    comLens = list(filter(lambda x:True if x > 0 else False,v))
    ans = 0
    for comLen in comLens:
        ans = ans + comLen ** 2 / seqLen ** 2

    w = 1 - np.sqrt(ans)
    return w


