from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 16})


def wc():
    t = np.arange(10, 358, 10, dtype=int)
    values = [9962, 11635, 11737, 1809, 6236, 6480, 2043, 10971, 11570, 11619, 1086, 10268, 12255, 12415, 12359, 12303, 509,
              9757, 11672, 11636, 11870, 5208, 3192, 8451, 8562, 8572, 3985, 5716, 5316, 5188, 12003, 11951, 9772, 11815, 11373]

    plt.plot(t, values, label="Throughput Workload C")
    plt.legend(loc="upper right", ncol=len(values))
    plt.title("Run throughput (ops/sec) of 2 shards with 3 replicas running in docker set at 1440 MTU while chos tool is running.")
    plt.ylabel("Throughput (ops/sec)")
    plt.xlabel("Time (sec)")
    plt.show()


def wbu():
    t = np.append(np.arange(10, 127, 10, dtype=int), 127)

    values = [10644, 11852, 11875, 11893, 11877, 11883, 12011,
              11972, 11927, 11923, 11823, 11870, 11154]
    plt.plot(t, values, label="Throughput Workload B")
    plt.legend(loc="upper right", ncol=len(values))
    plt.title(
        "Running workload B (uninterrupted) against 2 shards with 3 replicas running in docker set at 1440 MTU.")
    plt.ylabel("Throughput (ops/sec)")
    plt.xlabel("Time (sec)")
    plt.ylim(ymin=0, ymax=15000)

    plt.show()


def wbi():
    t = np.append(np.arange(10, 85, 10, dtype=int), 85)

    values = [7453, 5616, 1742, 7754, 379, 5625, 8709, 8636, 7969]
    plt.plot(t, values, label="Throughput Workload B")
    plt.legend(loc="upper right", ncol=len(values))
    plt.title(
        "Running workload B against 2 shards with 3 replicas running in docker while chaos tool is running set at 1440 MTU.")
    plt.ylabel("Throughput (ops/sec)")
    plt.xlabel("Time (sec)")
    plt.ylim(ymin=0, ymax=10000)

    plt.show()


def wbui():
    t = np.append(np.arange(10, 127, 10, dtype=int), 127)

    values = [10644, 11852, 11875, 11893, 11877, 11883, 12011,
              11972, 11927, 11923, 11823, 11870, 11154]
    t2 = np.append(np.arange(10, 85, 10, dtype=int), 85)

    values2 = [7453, 5616, 1742, 7754, 379, 5625, 8709, 8636, 7969]
    plt.plot(t, values, label="Throughput Workload B uninterrupted")
    plt.plot(t2, values2, label="Throughput Workload B w/chaos tool")
    plt.legend(loc="upper right", ncol=len(values2))
    plt.title(
        "")
    plt.ylabel("Throughput (ops/sec)")
    plt.xlabel("Time (sec)")
    plt.ylim(ymin=0, ymax=15000)

    plt.show()
    pass


wc()
wbu()
wbi()
