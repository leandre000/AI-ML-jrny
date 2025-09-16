import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# 🎨 Use scientific style for matplotlib
plt.style.use("seaborn-v0_8-darkgrid")

# -------------------------------
# SHM Function
# -------------------------------
def shm_motion(Xm, omega, t):
    """Return displacement, velocity, acceleration for SHM"""
    x = Xm * np.cos(omega * t)         # displacement
    v = -Xm * omega * np.sin(omega * t)  # velocity
    a = -Xm * (omega**2) * np.cos(omega * t)  # acceleration
    return x, v, a

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🌈 Simple Harmonic Motion Explorer")
st.markdown("For nursery kids to play & learn about SHM 📚🎵")

# User inputs
Xm = st.slider("Amplitude (Xm)", 0.1, 10.0, 5.0, 0.1)
omega = st.slider("Angular Frequency (ω)", 0.1, 10.0, 2.0, 0.1)
t_max = st.slider("Time duration (t)", 1, 20, 10)

# Generate time array
t = np.linspace(0, t_max, 500)
x, v, a = shm_motion(Xm, omega, t)

# -------------------------------
# 📊 Graphs of SHM
# -------------------------------
fig, ax = plt.subplots(figsize=(8,5))
ax.plot(t, x, label="Displacement (x)", color="royalblue", linewidth=2.5)
ax.plot(t, v, label="Velocity (v)", color="limegreen", linestyle="--")
ax.plot(t, a, label="Acceleration (a)", color="crimson", linestyle=":")
ax.set_title("📊 SHM Graphs", fontsize=16)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Value")
ax.legend()
st.pyplot(fig)

# -------------------------------
# 🌀 Animated Spring-Mass System
# -------------------------------
st.subheader("⚡ Animated Spring-Mass Motion")

frames = []
for i in range(len(t)):
    # Position of mass
    y_mass = -x[i]

    frames.append(
        go.Frame(
            data=[
                go.Scatter(x=[0,0], y=[0,y_mass], mode="lines", line=dict(width=4, color="black")),
                go.Scatter(x=[0], y=[y_mass-0.5], mode="markers",
                           marker=dict(size=40, color="orange", symbol="circle"))
            ],
            name=str(i)
        )
    )

fig_anim = go.Figure(
    data=[
        go.Scatter(x=[0,0], y=[0,-x[0]], mode="lines", line=dict(width=4, color="black")),
        go.Scatter(x=[0], y=[-x[0]-0.5], mode="markers",
                   marker=dict(size=40, color="orange", symbol="circle"))
    ],
    layout=go.Layout(
        xaxis=dict(range=[-2,2], showticklabels=False),
        yaxis=dict(range=[-Xm-2, Xm+2]),
        height=500,
        title="Spring-Mass Animation",
        updatemenus=[{
            "type": "buttons",
            "buttons": [
                {"label": "▶ Play", "method": "animate",
                 "args": [None, {"frame": {"duration": 40, "redraw": True}, "fromcurrent": True}]},
                {"label": "⏸ Pause", "method": "animate", "args": [[None], {"frame": {"duration": 0}}]}
            ]
        }]
    ),
    frames=frames
)

st.plotly_chart(fig_anim)
