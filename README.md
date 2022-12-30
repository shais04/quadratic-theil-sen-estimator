# quadratic-theil-sen-estimator
Extends the algorithm for the Theil–Sen linear estimator to a second-degree univariate polynomial.

The program `tester.py` provides 3 modes of testing: manual point entry, random data generation from a ground truth, and using a dataset from a file.
There are three example datasets in the folder `datasets` provided to test the estimator on:
* `KeplersThird.txt`, which for all 8 planets of the Solar System has orbital period in Earth years as the x variable and the mean distance to the sun cubed in AU^3 as the y variable (sourced from WolframAlpha Knowledgebase)
* `bluegills.txt`, which has age in years as the x variable and the length in mm of the fish as the y variable (sourced from [here](https://online.stat.psu.edu/stat462/node/159/), which in turn credits (Cook and Weisberg, 1999))
* `xsq.txt`, which has all integers from 1 through 10 as x variables and their squares as y variables, with the additional points (10, 7), (10, 42), and (10, 86)
