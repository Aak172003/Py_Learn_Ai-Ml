import numpy as np

# matplotlib is a library and pyplot is just a module
import matplotlib.pyplot as plt

# get value of sine(180)
print(np.sin(180))

# x value
x_sin = np.arange(0, 3 * np.pi, 0.1)
print("x_sin : ", x_sin)

# Calculate y for different sine, cos and tan

# ------------------------------ sine -----------------------------
y_sin = np.sin(x_sin)
print("y_sin : ", y_sin)

plt.plot(x_sin, y_sin)
plt.show()

# ------------------------------ cos -----------------------------

y_cos = np.cos(x_sin)
plt.plot(x_sin, y_cos)
plt.show()

# ------------------------------ tan -----------------------------

y_tan = np.tan(x_sin)
plt.plot(x_sin, y_tan)
plt.show()


