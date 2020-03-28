import json
import urllib

class CovidData:
    _covid_19_url = "https://api.rootnet.in/covid19-in/unofficial/covid19india.org"
    
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