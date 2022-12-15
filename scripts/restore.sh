#!/bin/bash

cd data
python ~/Software/File\ Utils/recursive_extract.py .
rmdir *
rm *.csv