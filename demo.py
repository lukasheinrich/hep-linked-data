import json
from pyld import jsonld
import rdflib

ctx = json.load(open('contexts/smpcontext.json'))
doc = json.load(open('samples/sample1.json'))

expanded = jsonld.expand(doc,options = {'expandContext': ctx})


#print(json.dumps(expanded, indent = 4))


g = rdflib.Graph()
for x in ['samples/sample1.json','samples/sample2.json']:
  g.parse(data = json.dumps(jsonld.expand(json.load(open(x)),options = {'expandContext': ctx})), format = 'json-ld')


print(g.serialize(format = 'json-ld').decode('utf-8'))
