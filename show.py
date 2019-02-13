import glob
import json
from pyld import jsonld
import rdflib
import click

ctx = json.load(open('contexts/context.json'))

@click.command()
@click.argument('identifier')
@click.option('--one/--many', default = False)
def frame(identifier, one):
    framed = jsonld.frame(json.load(open('./analysis.jsonld')), {'@context': ctx, "@id": identifier})                                                                                        
    click.secho(json.dumps(framed['@graph'] if not one else framed['@graph'][0],indent=4))


if __name__ == '__main__':
    frame()
