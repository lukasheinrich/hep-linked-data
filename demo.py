import glob
import json
from pyld import jsonld
import rdflib

ctx = json.load(open('contexts/context.json'))

g = rdflib.Graph()
for x in glob.glob('samples/*.json') + glob.glob('groups/*.json'):
  g.parse(data = json.dumps(jsonld.expand(json.load(open(x)),options = {'expandContext': ctx})), format = 'json-ld')

with open('analysis.ttl', 'w') as f:
    f.write(g.serialize(format = 'ttl').decode('utf-8'))

with open('analysis.jsonld','w') as f:
    f.write(g.serialize(format = 'json-ld').decode('utf-8'))

