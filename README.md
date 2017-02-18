# geomconvert
A python utility to convert between Cartesian and Z-matrix geometries. 

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

To convert from Z-matrix to XYZ (CURRENTLY IN DEVELOPMENT): 

python gc.py -zmat test.zmat

for files containing a Z-matrix

This assumes that the Z-matrix has values not variables for distances/angles/dihedrals. These can instead be assumed to be variables with the options

--rvar=True

--avar=True

--dvar=True

respectively. This will only work if all such quantities are given as variables, however.


