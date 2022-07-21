# UTILITY TO CONVERT BETWEEN XYZ AND Z-MATRIX GEOMETRIES
# Copyright 2017 Robert A Shaw
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software
# is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Usage: python3 gc.py -xyz [file to convert]
# or     python3 gc.py -zmat [file to convert]
# possible flags for zmatrix printing are:
# --rvar/avar/dvar = True/False
# --allvar = True/False (sets all above)

import numpy as np
import argparse
import gcutil as gc

parser = argparse.ArgumentParser()
parser.add_argument("-xyz", dest="xyzfile", required=False, type=str, help="File containing xyz coordinates")
parser.add_argument("-zmat", dest="zmatfile", required=False, type=str, help="File containing Z-matrix")
parser.add_argument("--rvar", dest="rvar", required=False, type=bool, default=False, help="Print distances as variables")
parser.add_argument("--avar", dest="avar", required=False, type=bool, default=False, help="Print angles as variables")
parser.add_argument("--dvar", dest="dvar", required=False, type=bool, default=False, help="Print dihedrals as variables") 
parser.add_argument("--allvar", dest="allvar", required=False, type=bool, default=False, help="Print all values as variables")
parser.add_argument("--precision", dest="precision", required=False, type=int, default=8, help="Sets the precision of coordinates and distances")
parser.add_argument("--angle_precision", dest="angle_precision", required=False, type=int, default=5, help="Sets the precision of angles")
args = parser.parse_args()

xyzfilename = args.xyzfile
zmatfilename = args.zmatfile
xyz = np.array
rvar = args.rvar or args.allvar
avar = args.avar or args.allvar
dvar = args.dvar or args.allvar
precision = args.precision
angle_precision = args.angle_precision

if (xyzfilename == None and zmatfilename == None):
    print("Please specify an input geometry")

elif (zmatfilename == None):
    xyzarr, atomnames = gc.readxyz(xyzfilename)
    distmat = gc.distance_matrix(xyzarr)
    gc.write_zmat(xyzarr, distmat, atomnames, rvar=rvar, avar=avar, dvar=dvar, distprecision=precision, angleprecision=angle_precision)
else:
    atomnames, rconnect, rlist, aconnect, alist, dconnect, dlist = gc.readzmat(zmatfilename)
    gc.write_xyz(atomnames, rconnect, rlist, aconnect, alist, dconnect, dlist, precision=precision)
