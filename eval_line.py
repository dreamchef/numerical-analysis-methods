def eval_line(x0, y0, x1, y1, alpha):
  
    slope = (y1 - y0) / (x1 - x0)
    y_intercept = y0 - slope * x0
    y_alpha = slope * alpha + y_intercept

    return y_alpha

# x0 = 1
# y0 = 2
# x1 = 4
# y1 = 5
# alpha = 2.5

# result = evaluate_line(x0, y0, x1, y1, alpha)
# print("The value of the line at alpha:", result)

# print(evaluate_line(0,0, 1, 1, 2))