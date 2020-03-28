# %%
import pandas as pd
import matplotlib as plt
import networkx as nx
from graph_analysis.CovidData import CovidData
covidgraph = CovidData().get_patient_graph()
nx.draw(covidgraph)

# %%
