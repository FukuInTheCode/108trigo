import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def taylor_series(x, n):
    result = 0
    for i in range(n):
        result += (-1)**i * x**(2*i + 1) / np.math.factorial(2*i + 1)
    return result

def update(val):
    n = int(slider.val)
    y = taylor_series(x, n)
    line.set_ydata(y)
    fig.canvas.draw_idle()

# Initial setup
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x)  # Function to approximate
n_init = 1  # Initial number of iterations

# Create plot
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
plt.title('Taylor Series Approximation')

# Plot the function
ax.plot(x, y, label='sin(x)')

# Plot the initial Taylor series approximation
line, = ax.plot(x, taylor_series(x, n_init), label=f'Taylor (n={n_init})', color='red')

# Add slider
ax_slider = plt.axes([0.15, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Iterations', valmin=1, valmax=20, valinit=n_init, valfmt='%d')

# Update plot when slider changes
slider.on_changed(update)

# Add legend
ax.legend()

plt.show()

