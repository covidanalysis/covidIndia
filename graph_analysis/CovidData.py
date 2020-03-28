import json
import urllib
import pandas as pd
import itertools
import networkx as nx

class CovidData:
    _covid_19_url = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org"
    graph = None
    dframe = None
    
    def get_covid_data_request(self):
        covid_19_req = urllib.request.Request(
            self._covid_19_url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        return covid_19_req
    
    def get_covid_json_data(self):
        req = self.get_covid_data_request()
        with urllib.request.urlopen(req) as url:
            data = json.loads(url.read().decode())
        return data
    
    def get_and_set_raw_data_frame(self):
        if self.dframe:
            return self.dframe
        covid_json = self.get_covid_json_data()
        dframe = pd.DataFrame.from_dict(covid_json["data"]["rawPatientData"])
        dframe["pid"] = dframe["patientId"].apply(lambda x: "P" + str(x))
        def to_edge(pid, links):
            return list(itertools.chain(*[[(pid,q) for q in qs["with"]] for qs in links]))
        dframe["edges"] = dframe.apply(lambda x: to_edge(x.pid, x.relationship), axis=1)
        self.dframe = dframe
        return self.dframe
    
    def get_patient_graph(self):
        if self.graph:
            return self.graph
        
        self.get_and_set_raw_data_frame( )
        
        edges = list(itertools.chain(*self.dframe.edges))
        G = nx.Graph()
        G.add_edges_from(edges)
        self.graph = G
        return self.graph