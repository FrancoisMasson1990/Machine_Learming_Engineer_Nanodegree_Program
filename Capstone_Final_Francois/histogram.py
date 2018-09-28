# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt


N = 3
Pneumonia = (3876, 9, 390)
Normal = (1342, 9, 234)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, Pneumonia, width, color='#d62728')
p2 = plt.bar(ind, Normal, width, bottom=Pneumonia)

plt.ylabel('# data')
plt.title('F1 score justification')
plt.xticks(ind, ('Train', 'Val', 'Test'))
plt.yticks(np.arange(0, 8000, 500))
plt.legend((p1[0], p2[0]), ('Pneumonia', 'Normal'))

plt.show()
