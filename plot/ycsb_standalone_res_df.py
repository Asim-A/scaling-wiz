import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'font.size': 16})


def iperf():
    dfPerf = pd.DataFrame([
        ["Send", 949, 910, 935, 910],
        ["Receive", 942, 916, 932, 913],
    ], columns=["Test type", "Normal", "Docker_MTU1500", "Docker_MTU1440", "Docker_MTU1450"])

    dfPerf.plot.barh(
        x="Test type", title="Bandwidth test (iperf3) of various network configurations")
    plt.xlabel("Bandwidth (Mbits/sec)")
    plt.legend(ncol=len(dfPerf.columns))
    plt.show()


def plotLoad():
    dfLoad = pd.DataFrame([
        ["Workload A", 28895, 22620, 24100, 24137,  24430],
        ["Workload B", 29728, 23948, 23972, 21973,  24870],
        ["Workload C", 28229, 23909, 23619, 23189,  24124]],
        columns=["Workloads", "Normal", "Docker MTU1500", "Docker MTU1340", "Docker MTU1450",  "Docker MTU1440"])

    print(dfLoad)
    dfLoad.plot.barh(x="Workloads",
                     title="Load throughput of various configurations of standalone MongoDB instances")
    plt.legend(ncol=len(dfLoad.columns))
    plt.xlabel("Throughput ops/sec")
    plt.show()


def plotLoadInitial():
    dfLoad = pd.DataFrame([
        ["Workload A", 28895, 22620],
        ["Workload B", 29728, 23948],
        ["Workload C", 28229, 23909]],
        columns=["Workloads", "Normal", "Docker MTU1500"]
    )
    dfLoad.plot.barh(x="Workloads",
                     title="Initial Load Throughput of standalone MongoDB instance (Normal vs. Standard Docker)")
    plt.legend(ncol=len(dfLoad.columns))
    plt.xlabel("Throughput (ops/sec)")
    plt.show()


def plotRunInitial():
    dfRun = pd.DataFrame([
        ["Workload A", 28040, 22022],
        ["Workload B", 27269, 24438],
        ["Workload C", 27327, 25341]],
        columns=["Workloads", "Normal", "Docker MTU1500"]
    )
    dfRun.plot.barh(x="Workloads",
                    title="Initial Run Throughput of standalone MongoDB instance (Normal vs. Standard Docker)")
    plt.legend(ncol=len(dfRun.columns))
    plt.xlabel("Throughput (ops/sec)")
    plt.show()
    pass


def plotRun():
    dfRun = pd.DataFrame([
        ["Workload A", 28040, 22022, 22322, 25176,  26965],
        ["Workload B", 27269, 24438, 23485, 22929,  26688],
        ["Workload C", 27327, 25341, 25104, 25433,  26839]],
        columns=["Workloads", "Normal", "Docker MTU1500", "Docker MTU1340", "Docker MTU1450", "Docker MTU1440"])

    print(dfRun)

    dfRun.plot.barh(
        x="Workloads", title="Run throughput of various configurations of standalone MongoDB instances")

    plt.legend(ncol=len(dfRun.columns))
    plt.xlabel("Throughput ops/sec")
    plt.show()


# plotLoad()
# plotRun()

iperf()
