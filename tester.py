from TheilSenRegression import quadratic_estimator
from time import time
import numpy as np
import matplotlib.pyplot as plt

def quadratic(a, b, c):
    return lambda x: a * x * x + b * x + c

def get_point(s, list1, list2): # returns whether to continue asking for points
    if s == "":
        if len(list1) < 3:
            print("You must enter at least 3 points.")
            return True
        return False
    try:
        loc = s.index(",")
        x, y = float(s[:loc]), float(s[loc + 1:])
        list1.append(x)
        list2.append(y)
    except:
        print("Unrecognized input. Please try again.")
    return True

def do_prediction(s): # return (predict again, can predict)
    if s == "":
        return (False, False)
    try:
        float(s)
        return (True, True)
    except:
        return (True, False)

def is_num(x):
    try:
        float(x)
        return True
    except:
        return False

def get_coeff(name):
    x = "nonnumeric"
    while not is_num(x):
        x = input(name + " = ")
        if not is_num(x):
            print("Non-numeric input. Please try again.")
    return float(x)

print("This program tests the quadratic Theil-Sen estimator algorithm on a list of points.")
while True:
    print("""Choose an option by entering the corresponding number:
    1. Manually enter your own data points
    2. Generate somewhat noisy data from a ground-truth curve
    3. Use data from a file
    4. Quit""")
    ans = input("")
    est = quadratic_estimator()
    X, y = [], []
    min_x, max_x = np.inf, -np.inf
    did_regression = False
    ground_truth = None

    if ans == "1":
        did_regression = True
        get_more = True
        while get_more:
            get_more = get_point(input("Enter a point in the form x,y: "), X, y)
            if len(X) > 0:
                min_x = min(min_x, X[-1])
                max_x = max(max_x, X[-1])
    
    elif ans == "2":
        did_regression = True
        print("Enter the coefficients of the ground truth curve ax^2 + bx + c:")
        a = get_coeff("a")
        b = get_coeff("b")
        c = get_coeff("c")
        print("Enter the boundaries of the range from which x values will be chosen at random in generating data.")
        x1 = get_coeff("x1")
        x2 = get_coeff("x2")
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        num_points = 0
        while not is_num(num_points) or num_points < 3:
            num_points = input("How many points? Must be at least 3. ")
            if is_num(num_points):
                num_points = int(num_points)
        ground_truth = quadratic(a, b, c)
        max_val = max(ground_truth(min_x), ground_truth(max_x))
        min_val = min(ground_truth(min_x), ground_truth(max_x))
        if min_x < -b/(2*a) < max_x:
            max_val = max(max_val, ground_truth(-b/(2*a)))
            min_val = min(min_val, ground_truth(-b/(2*a)))
        noise_factor = 0.07
        try:
            noise_factor = input("Give a factor for the noise (default is 0.07): ")
            noise_factor = float(noise_factor)
        except:
            noise_factor = 0.07
            print("Using the default noise factor of 0.07.")
        for i in range(num_points):
            x_val = np.random.uniform(min_x, max_x)
            y_val = ground_truth(x_val)
            y_val += np.random.normal(0, noise_factor * (max_val - min_val))
            X.append(x_val)
            y.append(y_val)

    elif ans == "3":
        did_regression = True
        filename = input("Enter the name of the file to use: ")
        try:
            with open(filename) as F:
                for line in F:
                    if (line.find(",") == -1):
                        did_regression = False
                        print("Unable to use your file as input. Make sure every line consists of comma-separated x and y values.")
                        break
                    xy = line.split(",")
                    try:
                        X.append(float(xy[0]))
                        y.append(float(xy[1]))
                        min_x = min(min_x, float(xy[0]))
                        max_x = max(max_x, float(xy[0]))
                    except:
                        did_regression = False
                        print("Unable to use your file as input. You might have non-numeric x or y values somewhere.")
                        break
        except:
            did_regression = False
            print("Unable to find the file {}.".format(filename))

    elif ans == "4":
        break
    
    else:
        print("Unrecognized option. Please try again.")

    if did_regression:
        try:
            start = time()
            coeffs = est.fit(X, y)
            end = time()
            print("Estimator coefficients (ax^2 + bx + c): [a, b, c] = {}".format(coeffs))
            print("Took {} ms.".format(round((end - start) * 1000)))
            option = (True, True)
            print("\nGive input to predict values. To terminate, enter nothing.")
            while option[0]:
                x_to_predict = input("Predict value for x = ")
                option = do_prediction(x_to_predict)
                if option[1]:
                    x_to_predict = float(x_to_predict)
                    print("The predicted value for x = {} is {}".format(x_to_predict, est.predict(x_to_predict)))
                elif option[0]:
                    print("Invalid input. Try again.")
            print("\nCreate a graph of the regression curve against the input points?")
            option = "A"
            while not (option == "Y" or option == "N"):
                option = input("Y (yes)/N (no): ").upper()
            if option == "Y":
                graph_min_x = min_x - 0.1 * (max_x - min_x)
                graph_max_x = max_x + 0.1 * (max_x - min_x)
                curve_x_vals = np.linspace(graph_min_x, graph_max_x, num = max(40, int(10 * (graph_max_x - graph_min_x))))
                curve_y_vals = est.predict(curve_x_vals)
                plt.clf()
                plt.plot(curve_x_vals, curve_y_vals, linewidth = 4, color = "springgreen", label = "Theil-Sen regression curve")
                if ans == "2":
                    truth_y_vals = ground_truth(curve_x_vals)
                    plt.plot(curve_x_vals, truth_y_vals, linestyle = "dashed", color = "black", label = "Ground truth curve")
                    plt.legend(loc="lower right")
                plt.plot(X, y, "co")
                plt.show()

        except:
            print("Unable to perform quadratic regression. Make sure your input has at least 3 points with distinct x-values.")

    print("")
