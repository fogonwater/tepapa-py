import requests

# A super-early stage Python wrapper for the Te Papa Collections API

class TePapa():
    def __init__(self, api_key=None, quiet=True):
        """Create a new API object, with the API Key and a flag for verbosity."""
        if api_key:
            self.api_key = api_key
        else:
            raise ValueError('Te Papa API requires an api key.')
        self.quiet = quiet

        self.headers = {
            'x-api-key': self.api_key,
            'Accept': 'application/json'
        }
        self.search_endpoint = 'https://data.tepapa.govt.nz/collection/search'

    def search(self, keyword):
        """ Make a keyword search to search endpoint"""
        params = {'q': keyword}
        r = requests.get(self.search_endpoint,
                         headers=self.headers, params=params)
        # TODO - handle bad requests
        return Results(r.json(), params)


class Results():
    def __init__(self, response, request):
        """ Create a results object"""
        self.request = request
        self.result_count = response['_metadata']['resultset']['count']
        self.results = response['results']
