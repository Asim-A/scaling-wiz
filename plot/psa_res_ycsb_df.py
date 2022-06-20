import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'font.size': 16})

def loadPSA():

    dfLoad = pd.DataFrame([
        ["Workload A", 15176, 13917, 14709],
        ["Workload B", 16385, 15262, 15869],
        ["Workload C", 15746, 14975, 15255]],
        columns=["Workloads", "Normal", "Docker MTU1500", "Docker MTU1440"])

    print(dfLoad)

    dfLoad.plot.barh(
        x="Workloads", title="Load throughput of various configurations of Primary-Secondary-Arbiter MongoDB instances")

    plt.legend(ncol=len(dfLoad.columns))
    plt.xlabel("Throughput (ops/sec)")
    plt.show()


def runPSA():
    dfRun = pd.DataFrame([
        ["Workload A", 23435, 20946, 21358],
        ["Workload B", 21769, 20634, 20374],
        ["Workload C", 20647, 22549, 21685]],
        columns=["Workloads", "Normal", "Docker MTU1500", "Docker MTU1440"])

    print(dfRun)

    dfRun.plot.barh(
        x="Workloads",  title="Run throughput of various configurations of Primary-Secondary-Arbiter MongoDB instances")

    plt.legend(ncol=len(dfRun.columns))
    plt.xlabel("Throughput (ops/sec)")
    plt.show()


loadPSA()
runPSA()
