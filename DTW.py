from DTW_v2 import *
from utils import *

float_formatter = lambda x: "%.2f" % x
np.set_printoptions(formatter={'float_kind': float_formatter})


def dtw_distance(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    df = np.full((l1, l2), np.inf)

    l = max(l1, l2)
    d = np.zeros(shape=(l, l))

    for i in range(l1):
        for j in range(l2):
            d[i, j] = (s1[i] - s2[j]) ** 2

    df[0, 0] = d[0][0]

    # 第一列
    for i in range(1, l1):
        df[i][0] = d[i][0] + df[i - 1][0]

    # 第一行
    for j in range(1, l2):
        df[0, j] = d[0][j] + df[0][j - 1]

    for i in range(1, l1):
        for j in range(1, l2):
            df[i, j] = d[i, j] + min(df[i - 1, j], df[i, j - 1], df[i - 1, j - 1])
    df = np.sqrt(df)
    return df[l1 - 1, l2 - 1], df.T


def dtw_distance_v2(df):
    w = compute_w(df)
    l = df.shape
    distance = df[l[0] - 1, l[1] - 1]
    return distance * w


if __name__ == '__main__':
    s1 = np.array([1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1])
    s2 = np.array([0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2, 0, 1, 1, 2])
    s3 = np.array([0.8, 1.5, 0, 1.2, 0, 0, 0.6, 1, 1.2, 0, 0, 1, 0.2, 2.4, 0.5, 0.4])

    res1, _1 = dtw_distance(s1, s2)
    res2, _2 = dtw_distance(s1, s3)

    # draw_seq(s1,s2,s3)
    print(f"the distance between s1 and s2 before updating：:{res1}")
    print(f"the distance between s1 and s3 before updating：:{res2}")

    if res1 < res2:
        print("v1中，s1 和 s2 更相似")
    else:
        print("v1中，s1 和 s3 更相似")

    dist1 = dtw_distance_v2(_1)
    dist2 = dtw_distance_v2(_2)
    print(f"the distance between s1 and s2 : {dist1}")
    print(f"the distance between s1 and s3 : {dist2}")
    if dist1 < dist2:
        print("v2中，s1 和 s2 更相似")
    else:
        print("v2中，s1 和 s3 更相似")

    # path = bestpath(_1)
    # draw_heatmap(_1, path)
    #
    # path2 = bestpath(_2)
    # draw_heatmap(_2,path2)
