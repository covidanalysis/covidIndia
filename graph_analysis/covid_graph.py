# %%
import pandas as pd
import matplotlib as plt
import networkx as nx
from graph_analysis.CovidDataGraph import CovidDataGraph
cvd = CovidDataGraph()
print(cvd.get_cluster_mean_degree())