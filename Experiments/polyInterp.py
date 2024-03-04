import numpy as np
import matplotlib.pyplot as plt

def polynInterp(x,y,degree=4):

    # Polynomial interpolation
    coefficients = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefficients)

    # Calculating the total squared error
    predicted_y = polynomial(x)
    squared_errors = (y - predicted_y) ** 2
    total_squared_error = np.sum(squared_errors)

    print(f"Total squared error: {total_squared_error}")

    # Generate a dense set of x for plotting the curve
    dense_x = np.linspace(min(x), max(x), 400)
    curve_y = polynomial(dense_x)

    # Generating polynomial equation as a string for the title
    poly_eq = "y = "
    for i, coeff in enumerate(polynomial.coefficients):
        power = len(polynomial.coefficients) - i - 1
        if power > 1:
            poly_eq += f"{coeff:.2f}x^{power} + "
        elif power == 1:
            poly_eq += f"{coeff:.2f}x + "
        else:
            poly_eq += f"{coeff:.2f}"

    return total_squared_error,  dense_x,  curve_y,  x,  y,  polynomial,  poly_eq



x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0])
y = np.array([22, 20.5, 19, 18.5, 18, 18, 18.5, 19, 21, 23, 24, 24.5, 25, 26, 27, 28, 28, 26, 24.5, 23, 22, 22, 21.5, 21, 22])

[TSE,dense_x,curve_y,x,y,polynomial,poly_eq] = polynInterp(x,y,4)

plt.figure(figsize=(10, 6))
plt.plot(dense_x, curve_y, label="Interpolated Curve", color='blue')
plt.scatter(x, y, color='red', label="Data Points")

# Drawing vertical lines from data points to curve
for x_, y_ in zip(x, y):
    plt.plot([x_, x_], [y_, polynomial(x_)], color='lightgrey', linestyle='-', linewidth=1)

plt.xlabel('x')
plt.ylabel('y')
plt.title(f'Polynomial Interpolation: {poly_eq}')

plt.legend()
plt.show()
