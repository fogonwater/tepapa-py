# TePapa.py

A super-early stage Python wrapper for the [Te Papa Collections API](https://github.com/te-papa/collections-api/wiki).

Very early stage and barely scratches surface of the API. Highly likely to change.

### Installation and dependencies.

- Tested with Python 3.7.x
- Uses [Requests](http://docs.python-requests.org/en/master/) library.

```
pip install -r requirements.txt
```

### Use

```python
from tepapa import TePapa
# create a new TePapa Collections object
>>> tp = TePapa(api_key='putYourApiKeyHere')

# Search for records with villages
>>> result = tp.search('village')

# see how many records in total set
>>> print("There are {} results.".format(result.result_count))

# display the results
>>> from pprint import pprint as pp
>>> pp(result.results)
```

### TODO

- pagination
- other endpoints
- error handling
- status messages
- rate limiting?
- everything else
