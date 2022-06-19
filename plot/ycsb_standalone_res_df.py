import matplotlib.pyplot as plt
import pandas as pd


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
    plt.show()


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
    plt.show()


plotRun()
