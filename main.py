from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


# %%
def ascii_histogram(seq) -> None:
    """A horizontal frequency-table/histogram plot."""
    counted = Counter(seq)
    for k in sorted(counted):
        print('{0:5f} {1}'.format(k, '+' * counted[k]))


# %%
stage2 = (
    1.7, 7.9, 7.3, 16.5, 6.0, 3.8, 4.5, 3.3, 3.7, 12.4, 0.7, 1.0, 0.7, 0.8, 0.6, 3.4, 0.8, 4.7, 2.6, 13.8, 3.3, 1.3,
    4.3, 1.9, 5.9, 12.3, 2.3, 1.7, 1.8, 1.9, 1.7, 3.4, 2.0, 4.9, 0.7, 0.8, 4.5, 1.1, 1.1, 9.9, 2.1, 1.1, 4.2, 2.3,
    0.7, 3.7, 1.8, 1.0)

stage2b = (
    1.68, 7.90, 7.25, 16.53, 5.98, 3.83, 4.45, 3.28, 3.70, 12.37, 0.67, 1.05, 0.63, 0.75, 0.62, 3.43, 0.78, 4.72, 2.63,
    13.78, 3.33, 1.27, 4.27, 1.83, 5.87, 12.30, 2.27, 1.70, 1.80, 1.88, 1.67, 3.38, 2.02, 4.90, 0.73, 0.75, 4.52, 1.13,
    1.08, 9.93, 2.12, 1.10, 4.18, 2.35, 0.72, 3.73, 1.80, 0.95
)
stage3 = (
    0.5, 1.6, 0.7, 1.2, 0.5, 0.7, 0.4, 0.5, 0.5, 0.5, 0.7, 0.4, 0.7, 0.4, 0.6, 0.4, 0.3, 0.3, 0.4, 0.7, 0.2, 0.4, 0.4,
    0.5, 1.0, 0.6, 0.9, 0.4, 0.4, 0.5, 0.6, 0.7, 0.7, 0.8, 0.3, 0.3, 0.3, 0.5, 0.4, 0.4, 0.5, 1.0, 0.6, 0.3, 0.3, 0.6,
    0.7, 0.6, 0.5, 0.5, 0.8, 0.5, 0.6, 0.6, 0.3, 0.8, 0.5, 0.5, 0.6, 0.2, 0.5, 0.4, 0.3, 0.4, 0.4, 0.6, 1.0, 0.9, 0.3,
    0.6, 0.3, 0.5, 1.0, 0.5, 0.3, 0.4, 0.8, 0.5, 0.5, 0.4, 0.3, 0.4, 0.6, 0.4, 0.5, 0.4, 0.3, 0.2)

stage3b = (
    0.52, 1.60, 0.68, 1.15, 0.48, 0.67, 0.42, 0.47, 0.47, 0.48, 0.65, 0.40, 0.68, 0.43, 0.58, 0.37, 0.27, 0.27,
    0.38, 0.72, 0.23, 0.38, 0.40, 0.53, 1.03, 0.63, 0.93, 0.42, 0.42, 0.53, 0.58, 0.70, 0.73, 0.77, 0.30, 0.30, 0.32,
    0.50, 0.37, 0.35, 0.53, 1.02, 0.57, 0.30, 0.33, 0.58, 0.72, 0.58, 0.48, 0.53, 0.78, 0.45, 0.57, 0.57, 0.27, 0.82,
    0.53, 0.48, 0.57, 0.22, 0.48, 0.35, 0.32, 0.40, 0.40, 0.58, 0.95, 0.87, 0.28, 0.55, 0.32, 0.52, 0.98, 0.53, 0.32,
    0.35, 0.80, 0.47, 0.45, 0.40, 0.28, 0.43, 0.63, 0.43, 0.52, 0.43, 0.28, 0.25
)

# Add average and deviation

# %%
ascii_histogram(stage2)
print("---")
ascii_histogram(stage3)
# %%
n, bins, patches = plt.hist(x=stage2, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time (mins)')
plt.ylabel('Frequency')
plt.title('Labeling for Stage2')
maxfreq = n.max()

# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()
# %%
n, bins, patches = plt.hist(x=stage3, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time (mins)')
plt.ylabel('Frequency')
plt.title('Labeling for Stage3')
maxfreq = n.max()

# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()

# %%
n, bins, patches = plt.hist(x=stage2b, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time (mins)')
plt.ylabel('Frequency')
plt.title('Labeling for Stage2')
maxfreq = n.max()

# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()

# %%
n, bins, patches = plt.hist(x=stage3b, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time (mins)')
plt.ylabel('Frequency')
plt.title('Labeling for Stage3')
maxfreq = n.max()

# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()

# %%
stage2_labels = (
    0.42, 1.58, 1.81, 3.31, 1.50, 0.96, 4.45, 0.82, 1.23, 0.67, 0.26, 0.16, 0.25, 0.62, 1.14, 0.26, 0.59, 0.53, 1.25,
    0.56, 0.21, 0.36, 0.26, 0.53, 1.03, 0.17, 0.13, 0.18, 0.19, 0.15, 0.34, 0.22, 0.61, 0.15, 0.11, 0.75, 0.23, 0.18,
    1.99, 0.42, 0.22, 1.05, 0.34, 0.12, 0.47, 0.60, 0.24,
)

stage3_labels = (
    0.04, 0.32, 0.09, 0.38, 0.10, 0.11, 0.06, 0.09, 0.12, 0.06, 0.06, 0.03, 0.14, 0.09, 0.12, 0.12, 0.04, 0.05, 0.08,
    0.14, 0.05, 0.03, 0.06, 0.13, 0.34, 0.13, 0.19, 0.10, 0.08, 0.07, 0.05, 0.07, 0.24, 0.19, 0.10, 0.06, 0.06, 0.06,
    0.05, 0.09, 0.11, 0.34, 0.11, 0.06, 0.07, 0.10, 0.18, 0.07, 0.04, 0.11, 0.13, 0.05, 0.09, 0.09, 0.07, 0.14, 0.18,
    0.05, 0.08, 0.01, 0.16, 0.07, 0.06, 0.06, 0.07, 0.12, 0.16, 0.22, 0.04, 0.14, 0.08, 0.17, 0.16, 0.08, 0.05, 0.12,
    0.11, 0.16, 0.09, 0.07, 0.06, 0.11, 0.13, 0.11, 0.06, 0.09, 0.04, 0.04,
)

# %%
n, bins, patches = plt.hist(x=stage2_labels, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time (mins)')
plt.ylabel('Frequency')
plt.title('Labeling for Stage2')
maxfreq = n.max()

# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)

plt.show()

# %%
n, bins, patches = plt.hist(x=stage3_labels, bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Time (mins)')
plt.ylabel('Frequency')
plt.title('Labeling for Stage3')
maxfreq = n.max()

# Set a clean upper y-axis limit.
plt.ylim(ymax=np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else maxfreq + 10)
plt.show()
