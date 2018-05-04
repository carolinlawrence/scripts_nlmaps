NLmaps Scripts
--------------

A few scripts that help with processing the [NLmaps corpus](http://www.cl.uni-heidelberg.de/statnlpgroup/nlmaps/).

Linearisation and Reversing it
------------------------------
Original NLmaps queries are written in a bracket form which can be linearised into individual tokens by taking a pre-order tree traversal.
For example, the query

``query(north(area(keyval('name','Paris')),nwr(keyval('building','cathedral'))),qtype(latlong))``

can be linearised to

``query@2 north@2 area@1 keyval@2 name@0 Paris@s nwr@1 keyval@2 building@0 cathedral@s qtype@1 latlong@0``

We provide two scripts that handle the conversion, one for each direction. The idea for linearisation was originally presented by 
[Andreas et al., 2013.](http://people.eecs.berkeley.edu/~jda/papers/avc_smt_semparse.pdf)
Thus, the code in this repo is a modified version of their repo [smt-semparse](https://github.com/jacobandreas/smt-semparse) and additionally contains NLmaps specific components.

To linearise a file of NLmaps queries, use:

``python linearise.py -i input_file -o output_file``

and to reverse the linearisation, use:

``python functionalise.py -i input_file -o output_file``

Evaluation
----------
NLmaps can either be evaluated at the query sequence level or based on the answers if queries are executed against an instance of the OpenStreetMap database.

To validate at the sequence level, use:

``python seq_eval.py -i suggested_queries_file -g gold_queries_file``

and to validate at the answer level, use:

``python eval.py -i suggested_answers_file -g gold_answers_file``

To validate at the answer level, an instance of the OpenStreetMap database needs to be [installed](http://wiki.openstreetmap.org/wiki/Overpass_API/Installation#Populating_the_DB) as well as [overpass-nlmaps](https://github.com/carhaas/overpass-nlmaps).
