=======
 SVMPy
=======

--------------
 Introduction
--------------

This is a basic implementation of a soft-margin kernel SVM solver in
Python using `numpy` and `cvxopt`.


--------------
 Demonstration
--------------

Run `bin/svm-py-demo --help`.  

::
   
  ∴ bin/svm-py-demo --help
  usage: svm-py-demo [-h] [--num-samples NUM_SAMPLES]
                     [--num-features NUM_FEATURES] [-g GRID_SIZE] [-f
                     FILENAME]
  
  optional arguments:
    -h, --help            show this help message and exit
    --num-samples NUM_SAMPLES
    --num-features NUM_FEATURES
    -g GRID_SIZE, --grid-size GRID_SIZE
    -f FILENAME, --filename FILENAME
  

For example,

::

  bin/svm-py-demo --num-samples=100 --num-features=2 --grid-size=500 --filename=svm500.pdf

yields the image

.. image:: http://i.imgur.com/yy0oUVk.png

