===========
fastGraph
===========

A fast and lightweight package designed for Graph Embedding.
Built for DeepWalk, node2vec walk and likely walk(sampled with edges of transition probability).
Built for both undirected, directed and both weighted-, binary-edge graph.


Dev Usage
-------
::

  python fastGraph/__main__.py --input example_graph/wiki-Vote.csv --output example_graph/wiki-Vote.model
  --walk-type node2vec --ngram 1 --number-paths 5 --embed-size 64 --path-length 40

Package Installation & Usage
-------
``cd fastGraph``

``pip install -r requirements.txt``

::

  fastGraph --input example_graph/wiki-Vote.csv --output example_graph/wiki-Vote.model
  --walk-type node2vec --ngram 1 --number-paths 5 --embed-size 64 --path-length 40

Pip Installation
-------
``pip install fastGraph``

Dataset
-------
There are various graph dataset available on the internet, for example here's a collection_ from Stanford.
.. _collection: https://snap.stanford.edu/data/

Acknowledgement
-------
Inspired by the great work from deepwalk_.

.. _deepwalk: https://github.com/phanein/deepwalk
