# The Simpsons characters network analysis

An analysis of the network of characters in The Simpsons

![preview1](https://cloud.githubusercontent.com/assets/6751845/24168281/9ee04398-0e71-11e7-919d-ce25bf4773f3.png)

## Dataset
The original dataset is from https://github.com/sghall/simpsons-episode-data with thanks to [Delimited Technologies](www.delimited.io)

The dataset can be found in /support, it consists of two main files.
  - <i>simpsonsNodes.csv</i>
    - the names of characters in the Simpsons with a description and Id
  - <i>simpsonsEdges.csv</i>
    - a source and target Id for the two characters who appear together along with a weight corresponding to the number of times they appear together
  - <i>simpsons_ep-char.csv</i>
    - original dataset that contains every episode and the characters who appear in them

Also in the /support are two python files.
  - <i>data.py</i>
    - converts the simpsons_ep-char.csv file into simpsonsEdges.csv without the weights
  - <i>data2.py</i>
    - adds the weights to rows in simpsonsEdges.csv

## Analysis
The analysis of the network was done using [Gephi](https://gephi.org/) an open-source graph visualisation tool.

The report was produced for the coursework and contains the full analysis and many screenshots of the network from Gephi.
