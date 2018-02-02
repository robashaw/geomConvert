# geomconvert
A python utility to convert between Cartesian and Z-matrix geometries. 

RECENTLY ADDED: when converting from zmat to xyz, variables can now be read with no caveats.

Running the below will print the output to the standard output stream (i.e. the terminal in most cases); this can be piped into a file in the usual way, e.g.

python gc.py -xyz test.xyz > test.zmat

## Usage

To convert from XYZ to Z-matrix:

python gc.py -xyz test.xyz 

for files in XYZ format, i.e.

Number of atoms

TITLE CARD

Atom x y z

Atom x y z

...

The default is to print the values of distances/angles/dihedrals. These can instead be printed as variables with the options

--rvar=True
--avar=True
--dvar=True

respectively.

To convert from Z-matrix to XYZ:

python gc.py -zmat test.zmat

for files containing a Z-matrix. This no longer assumes that the Z-matrix has values not variables for distances/angles/dihedrals, and can read variables with no additional options. 


