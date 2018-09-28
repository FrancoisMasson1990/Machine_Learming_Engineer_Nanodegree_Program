# a stacked bar plot with errorbars

import matplotlib.pyplot as plt
#plt.plot([9935, 3124 , 2957, 1200, 3310], [0.625,0.831,0.785,0.657,0.713], 'ro')
plt.plot(9935, 0.625,'bo',label='Vanilla CNN')
plt.plot(3124,0.831,'ro',label='Optimized CNN + Adam')
plt.plot (2957,0.785,'go',label='Optimized CNN + SGD')
plt.plot(1200,0.657,'yo',label='InceptionV3')
plt.plot(3310,0.713,'ko',label='InceptionV3 + Fine tuning')
plt.axis([0, 10000, 0.5, 1])
plt.title('F1 score for 25 epochs VS time to train the model')
plt.ylabel('F1 Score')
plt.xlabel('Time to train the model (s)')
plt.legend()
plt.show()

