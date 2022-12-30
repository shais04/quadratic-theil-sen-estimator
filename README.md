# quadratic-theil-sen-estimator
Extends the algorithm for the Theil–Sen linear estimator (which you can read about [here](https://en.wikipedia.org/wiki/Theil%E2%80%93Sen_estimator)) to a second-degree univariate polynomial.

To extend the algorithm for quadratic regression, a formula was derived for the leading coefficient $a$ in the quadratic function $f(x) = ax^2+bx+c$ that goes through the points $(x_1, y_1)\text{, }(x_2,y_2)\text{, and }(x_3,y_3)$. This formula is $\displaystyle a = \frac{y_1d_1 + y_2d_2 + y_3d_3}{x_1^2d_1 + x_2^2d_2 + x_3^2d_3}$, where $d_1 = x_2-x_3\text{, }d_2 = x_3-x_1\text{, and }d_3 = x_1-x_2$.

The program `tester.py` provides 3 modes of testing: manual point entry, random data generation from a ground truth, and using a dataset from a file.
There are three example datasets in the folder `datasets` provided to test the estimator on:
* `KeplersThird.txt`, which for all 8 planets of the Solar System has orbital period in Earth years as the x variable and the mean distance to the sun cubed in AU^3 as the y variable (sourced from WolframAlpha Knowledgebase)
* `bluegills.txt`, which has age in years as the x variable and the length in mm of the fish as the y variable (sourced from [here](https://online.stat.psu.edu/stat462/node/159/), which in turn credits (Cook and Weisberg, 1999))
* `xsq.txt`, which has all integers from 1 through 10 as x variables and their squares as y variables, with the additional points (10, 7), (10, 42), (10, 86), and (9, 21)
