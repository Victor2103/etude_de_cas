#!bin/bash

mkdir data1 && cd data1
wget http://data.vision.ee.ethz.ch/cvl/food-101.tar.gz
tar -xf food-101.tar.gz
rm food-101.tar.gz