import numpy as np

def F(x):
    return np.array([x[0]+np.cos(x[0]*x[1]*x[2]) - 1,
                (1-x[0])**(1/4)+x[1]+0.05*x[2]**2 - 0.15*x[2] - 1,
                -x[0]**2 - 0.1*x[1]**2 + 0.01*x[1] + x[2] - 1]);

def J(x):
    return np.array([[-x[1]*x[2]*np.sin(x[0]*x[1]*x[2]) + 1, -x[0]*x[2]*np.sin(x[0]*x[1]*x[2]), -x[0]*x[1]*np.sin(x[0]*x[1]*x[2])],
                [-0.25*(1 - x[0])**(-0.75), 1, 0.1*x[2] - 0.15],
                [-2*x[0], 0.01 - 0.2*x[1], 1]]);

# Steepest Descent Method
def steepest_descent(F, J, x0, max_iter=1000, tolerance=1e-6):
    x = x0
    for i in range(max_iter):
        f_val = F(x)
        j_val = J(x)
        
        # Check if the current function values are close to zero
        if np.linalg.norm(f_val) < tolerance:
            return x, i
        
        # The descent direction is the negative of the Jacobian matrix multiplied by the function values
        descent_direction = -np.matmul(j_val.T, f_val)
        
        # Line search to find the optimal step size (alpha)
        # For simplicity, we're using a constant step size here
        alpha = 1e-3
        
        # Update the estimate
        x = x + alpha * descent_direction
        
    return x, max_iter

# Initial guess
x0 = np.array([1.0, 1.0, -1.0])

# Run the Steepest Descent Method
solution, iterations = steepest_descent(F, J, x0)

print(f'Solution: {solution}')
print(f'Iterations: {iterations}')