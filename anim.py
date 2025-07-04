# или pygame для рендеринга
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
plt.switch_backend('TkAgg')
fig, ax = plt.subplots()
xdata, ydata = [], []
line, = ax.plot([], [], 'ro', animated=True)
ax.set_xlim(-1, 10)
ax.set_ylim(-1.5, 1.5)
def init():
    line.set_data(xdata, ydata)
    return line,

# Обновление графика для каждого кадра
def update(frame):
    xdata.append(frame) # Значение по X
    ydata.append(np.sin(frame))
    line.set_data(xdata, ydata)
    return line, # Обнволённая линия

# Запуск анимации
ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100), interval=50, blit=True, init_func=init)
plt.show()