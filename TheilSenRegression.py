from statistics import median

# Throw an error when the data to fit has an issue
class FitError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

# Included for comparison
class linear_estimator:
    """
    Initializes the estimator. Sets all the weights to None.
    """
    def __init__(self):
        self.a = None
        self.b = None
    
    """
    Fits the estimator to the points (X[i], y[i]).
    Returns a list [a, b] corresponding to the coefficients in ax + b.
    """
    def fit(self, X, y):
        if len(X) != len(y):
            raise FitError("Lists X and y must be of the same length.")
        if len(set(X)) < 2:
            raise FitError("There must be at least 2 distinct values in the array X for linear regression.")
        xy = [[X[i], y[i]] for i in range(len(X))]
        coeffs = []
        for i in range(len(xy) - 1):
            for j in range(i + 1, len(xy)):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                if x1 != x2:
                    coeffs.append((y2 - y1) / (x2 - x1))
        self.a = median(coeffs)
        coeffs = []
        for pt in xy:
            pt[1] -= self.a * pt[0]
            coeffs.append(pt[1])
        self.b = median(coeffs)
        del(coeffs)
        return [self.a, self.b]

    """
    Uses the computed weights to estimate a value given an input.
    """
    def predict(self, x):
        return self.a * x + self.b

class quadratic_estimator:
    """
    Initializes the estimator. Sets all the weights to None.
    """
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    """
    Fits the estimator to the points (X[i], y[i]).
    Returns a list [a, b, c] corresponding to the coefficients in ax^2 + bx + c.
    """
    def fit(self, X, y):
        if len(X) != len(y):
            raise FitError("Lists X and y must be of the same length.")
        if len(set(X)) < 3:
            raise FitError("There must be at least 3 distinct values in the array X for quadratic regression.")
        xy = [[X[i], y[i]] for i in range(len(X))]
        coeffs = []
        for i in range(len(xy) - 2):
            for j in range(i + 1, len(xy) - 1):
                for k in range(j + 1, len(xy)):
                    x1, y1 = xy[i]
                    x2, y2 = xy[j]
                    x3, y3 = xy[k]
                    d1, d2, d3 = x2 - x3, x3 - x1, x1 - x2
                    if d1 * d2 * d3 != 0:
                        coeffs.append((y1 * d1 + y2 * d2 + y3 * d3) / (x1 * x1 * d1 + x2 * x2 * d2 + x3 * x3 * d3))
        self.a = median(coeffs)
        coeffs = []
        for pt in xy:
            pt[1] -= self.a * pt[0] * pt[0]
        for i in range(len(xy) - 1):
            for j in range(i + 1, len(xy)):
                x1, y1 = xy[i]
                x2, y2 = xy[j]
                if x1 != x2:
                    coeffs.append((y2 - y1) / (x2 - x1))
        self.b = median(coeffs)
        coeffs = []
        for pt in xy:
            pt[1] -= self.b * pt[0]
            coeffs.append(pt[1])
        self.c = median(coeffs)
        del(coeffs)
        return [self.a, self.b, self.c]

    """
    Uses the computed weights to estimate a value given an input.
    """
    def predict(self, x):
        return self.a * x * x + self.b * x + self.c
