from statistics import median

# Throw an error when the data to fit has an issue
class FitError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

# Included for comparison
class linear_estimator:
    
    def __init__(self):
        """
        Initializes the estimator. Sets all the weights to None.
        """
        self.a = None
        self.b = None
    
    def fit(self, X, y):
        """
        Fits the estimator to the points (X[i], y[i]).
        Returns a list [a, b] corresponding to the coefficients in ax + b.
        """
        if len(X) != len(y):
            raise FitError("Lists X and y must be of the same length.")
        if len(set(X)) < 2:
            raise FitError("There must be at least 2 distinct values in the array X for linear regression.")
        coeffs = []
        for i in range(len(X) - 1):
            x1, y1 = X[i], y[i]
            for j in range(i + 1, len(X)):
                x2, y2 = X[j], y[j]
                if x1 != x2:
                    coeffs.append((y2 - y1) / (x2 - x1))
        self.a = median(coeffs)
        coeffs = []
        for i in range(len(X)):
            coeffs.append(y[i] - self.a * X[i])
        self.b = median(coeffs)
        del(coeffs)
        return [self.a, self.b]

    def predict(self, x):
        """
        Uses the computed weights to estimate a value given an input.
        """
        return self.a * x + self.b

class quadratic_estimator:
    
    def __init__(self):
        """
        Initializes the estimator. Sets all the weights to None.
        """
        self.a = None
        self.b = None
        self.c = None

    def fit(self, X, y):
        """
        Fits the estimator to the points (X[i], y[i]).
        Returns a list [a, b, c] corresponding to the coefficients in ax^2 + bx + c.
        """
        if len(X) != len(y):
            raise FitError("Lists X and y must be of the same length.")
        if len(set(X)) < 3:
            raise FitError("There must be at least 3 distinct values in the array X for quadratic regression.")
        coeffs = []
        for i in range(len(X) - 2):
            x1, y1 = X[i], y[i]
            for j in range(i + 1, len(X) - 1):
                x2, y2 = X[j], y[j]
                d3 = x1 - x2
                for k in range(j + 1, len(X)):
                    x3, y3 = X[k], y[k]
                    d1, d2 = x2 - x3, x3 - x1
                    if d1 * d2 * d3 != 0:
                        coeffs.append((y1 * d1 + y2 * d2 + y3 * d3) / (x1 * x1 * d1 + x2 * x2 * d2 + x3 * x3 * d3))
        self.a = median(coeffs)
        coeffs = []
        for i in range(len(X) - 1):
            x1, y1 = X[i], y[i] - self.a * X[i] * X[i]
            for j in range(i + 1, len(X)):
                x2, y2 = X[j], y[j] - self.a * X[j] * X[j]
                if x1 != x2:
                    coeffs.append((y2 - y1) / (x2 - x1))
        self.b = median(coeffs)
        coeffs = []
        for i in range(len(X)):
            coeffs.append(y[i] - self.a * X[i] * X[i] - self.b * X[i])
        self.c = median(coeffs)
        del(coeffs)
        return [self.a, self.b, self.c]

    def predict(self, x):
        """
        Uses the computed weights to estimate a value given an input.
        """
        return self.a * x * x + self.b * x + self.c
