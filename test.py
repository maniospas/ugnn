from ugnn import tasks
from ugnn import architectures
from ugnn.utils import training
import torch
import numpy as np
import random
from datetime import datetime
import sys


starting_time = datetime.now()
setting = "cora"  # (cora | citeseer | pubmed | diffusion | propagation | degree | triangle | square)  [overtrain]
compare = [
    #architectures.MLP,
    #architectures.GCN,
    #architectures.GCNII,
    #architectures.APPNP,
    architectures.UniversalP,
]
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device:".ljust(10) + str(device))


def run(Model, task, splits, **kwargs):
    model = Model(task.feats, task.classes).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)
    acc = training(
        model=model,
        optimizer=optimizer,
        verbose=model.__class__.__name__,
        **splits,
        **kwargs,
    )
    # print()
    return acc


# make comparisons
results = [list() for _ in compare]
print("Setting:".ljust(10) + setting)
print(" ".join([architecture.__name__.ljust(8) for architecture in compare]))
for _ in range(5):
    if "diffusion" in setting:
        task = tasks.DiffusionTask(
            nodes=100, max_density=0.1, graphs=100, alpha=random.uniform(0, 0.5)
        ).to(device)
    elif "propagation" in setting:
        task = tasks.PropagationTask(
            nodes=100, max_density=0.1, graphs=100, alpha=random.uniform(0, 0.5)
        ).to(device)
    elif "degree" in setting:
        task = tasks.DegreeTask(nodes=100, max_density=0.1, graphs=100).to(device)
    elif "triangle" in setting:
        task = tasks.TrianglesTask(nodes=100, max_density=0.1, graphs=100).to(device)
    elif "square" in setting:
        task = tasks.SquareCliqueTask(nodes=20, max_density=0.5, graphs=100).to(device)
    elif "cora" in setting:
        task = tasks.PlanetoidTask("Cora", device)
    elif "citeseer" in setting:
        task = tasks.PlanetoidTask("Citeseer", device)
    elif "pubmed" in setting:
        task = tasks.PlanetoidTask("Pubmed", device)
    else:
        raise Exception("invalid setting")

    # from matplotlib import pyplot as plt
    # plt.hist(task.labels.cpu().numpy(), bins=task.classes)
    # plt.show()

    splits = task.overtrain() if "overtrain" in setting else task.split()
    for architecture, result in zip(compare, results):
        result.append(float(run(architecture, task, splits)))
    print("\r".ljust(80), end="")
    print("\r"+" ".join([f"{result[-1]:.3f}".ljust(8) for result in results]))

def printall():
    print(" ".join([architecture.__name__.ljust(8) for architecture in compare]))
    print(" ".join([f"{np.mean(result):.3f}".ljust(8) for result in results]))
    print("Standard deviations")
    print(" ".join([f"{np.std(result):.3f}".ljust(8) for result in results]))
    from scipy.stats import rankdata
    ranks = len(compare)+1-rankdata(np.array(results), axis=0).T
    ranks = ranks.mean(axis=0)
    print("Nemenyi ranks")
    print(" ".join([f"{rank:.3f}".ljust(8) for rank in ranks]))


print("\n==== Summary ====")
printall()
with open(f'results/{setting} [{str(starting_time).replace(":", "-")}].txt', 'w') as sys.stdout:
    printall()
