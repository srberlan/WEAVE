# WEAVE
Templates for creating source catalogues for WEAVE-MOS observations

There are two Python files provided, adapted for specific WEAVE survey needs (SCIP). You only need to modify and run createFits.py; simply keep the other file (createCols.py) in the same directory.

The code is designed to be self-explanatory: read your data and include each column as a vector when prompted. Please note that several columns are mandatory. Other columns may be left empty if you do not have the information, but it is best to provide as much detail as possible.

Once you have integrated your data, run the script using:

python createFits.py

The output is a FITS catalogue, which you can then use to create your Observing Blocks. If you need to adapt these scripts for a different MOS survey or program, simply modify the specific column definitions in both files to generate your preferred WEAVE template.
