import matplotlib.pyplot as plt
import numpy as np

R_single = 1.2
delta_r_single = 0.1
f_single = 15
p_single = 0

theta = np.linspace(0, 2*np.pi, 1000)

x_single = R_single * (1 + delta_r_single * np.sin(f_single * theta + p_single)) * np.cos(theta)
y_single = R_single * (1 + delta_r_single * np.sin(f_single * theta + p_single)) * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x_single, y_single)
plt.axis('equal')
plt.title('Single Curve')
plt.show()

delta_r = 0.05

plt.figure(figsize=(10, 10))
for i in range(1, 11):
    R = i

    f = 2 + in r
    p = np.random.uniform(0, 2*np.pi)

    x = R * (1 + delta_r * np.sin(f * theta + p)) * np.cos(theta)
    y = R * (1 + delta_r * np.sin(f * theta + p)) * np.sin(theta)

    plt.plot(x, y, label=f'p = {p}')

plt.axis('equal')
plt.title('10 Curves')
plt.legend()
plt.show()