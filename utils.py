import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def draw_seq(s1, s2, s3):
    t1 = np.arange(0, len(s1))
    t2 = np.arange(0, len(s2))
    t3 = np.arange(0, len(s3))

    plt.figure(1)
    plt.subplot(311)
    plt.plot(t1, s1)
    plt.subplot(312)
    plt.plot(t2, s2)
    plt.subplot(313)
    plt.plot(t3, s3)

    plt.show()


def draw_heatmap(data,path):
    # sns.heatmap(data,annot=False,cmap="YlGnBu")
    sns.heatmap(data, annot=False)
    x = [i+0.5 for i,j in path]
    y = [j+0.5 for i, j in path]
    plt.plot(y,x,color='green', marker='o')
    plt.show()

