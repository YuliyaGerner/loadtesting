import json
from pprint import pprint

with open("product-req.json", 'r', encoding='utf8') as f:
	data = f.read()
	serialized_data = json.loads(data)
	pprint(serialized_data)