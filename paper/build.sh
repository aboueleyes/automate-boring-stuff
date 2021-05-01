#!/usr/bin/bash

./data_generate.py 
./plot.py -i data.dat -o plot-data.png 
pdflatex paper.tex 
zathura paper.pdf 