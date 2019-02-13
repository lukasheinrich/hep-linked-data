all:
	python demo.py
	python ontology-visualization/ontology_viz.py -o analysis.dot analysis.ttl
	dot -Tpng analysis.dot  > analysis.png

