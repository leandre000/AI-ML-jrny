import numpy as np
import matplotlib.pyplot as plt

# Parameters
phi = 0                 # phase angle (rad)
xm = 1                  # amplitude of displacement
w = 2 * np.pi           # angular frequency (rad/s)
t = np.linspace(0, 2, 1000)  # time from 0 to 2s

# SHM equations
x = xm * np.sin(w * t + phi)                  # displacement
vm = w * xm                                   # velocity amplitude
v = vm * np.sin(w * t + phi + np.pi/2)        # velocity = derivative of displacement
am = w**2 * xm                                # acceleration amplitude
a = -am * np.sin(w * t + phi)                 # acceleration = derivative of velocity

# Plotting
plt.figure(figsize=(10,6))
plt.axhline(0, color="black", linewidth=0.8)

plt.plot(t, x, label=r'$x(t)$: Displacement', color="blue", linewidth=2)
plt.plot(t, v, label=r'$v(t)$: Velocity', color="green", linestyle="--", linewidth=2)
plt.plot(t, a, label=r'$a(t)$: Acceleration', color="red", linestyle=":", linewidth=2)

plt.axvspan(0, 1, color="gray", alpha=0.1, label="1 cycle (T=1s)")

plt.title("Simple Harmonic Motion (x, v, a vs time)", fontsize=14, fontweight="bold")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
