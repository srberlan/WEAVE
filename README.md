# WEAVE
Templates for creating source catalogues for WEAVE-MOS observations

There are two python files, adopted to an specific WEAVE survey needs (SCIP). You only need to modify and run the createFits.py. Just have the other one (createCols.py) in the same directory. The code should be self explanatory, but basically you need to read your data and include each of the columns as a vectors when requested. You will see that some columns are mandatory: make sure you fill those. The other ones can be left empty if you do not have the information, but try to fill as much as possible.
Once the file is filled with your data, just run the code as: python createFits.py. The output of running the code is a fits catalogue, from which you can create your Observing Blocks.

In case you need to adapt the codes to another MOS survey/program, just modify the specific columns in both codes for generating your prefered WEAVE template.
