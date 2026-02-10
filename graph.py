import matplotlib.pyplot as plt
import numpy as np

positions = np.arange(1, 101)

avg = np.concatenate(
    [
        np.full(80, 39),  # Avg between 38 and 40
        np.full(10, 32),  # Fixed value 32
        np.full(10, 6),  # Avg between 2 and 10
    ]
)

superior = np.concatenate([np.full(80, 40), np.full(10, 32), np.full(10, 10)])
inferior = np.concatenate([np.full(80, 38), np.full(10, 32), np.full(10, 2)])

plt.figure(figsize=(12, 6))

plt.fill_between(
    positions,
    inferior,
    superior,
    color="skyblue",
    alpha=0.4,
    label="Simulation Range",
)

plt.plot(positions, avg, color="navy", lw=2, label="Average Estimated Quality")

plt.axhspan(28, 42, color="green", alpha=0.05)
plt.axhspan(20, 28, color="orange", alpha=0.05)
plt.axhspan(0, 20, color="red", alpha=0.05)

plt.title("Dynamic Quality Profile: Phred33 Simulation", fontsize=14)
plt.xlabel("Base Pair(bp)")
plt.ylabel("Phred Score (Q)")
plt.ylim(0, 45)
plt.legend(loc="lower left")
plt.grid(True, linestyle="--", alpha=0.5)

plt.show()
