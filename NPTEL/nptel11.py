"""problem on plotting"""
'''crowd computing'''

import matplotlib.pyplot as plt
import statistics
estimate=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,3,4,5,6,7,8,6,5,4,2,8,4,3,5,7,3,2,5,7,4,2,5,8,5,1,4,6,8,5,3,1,4,7,8,4,2,5,7]

estimate.sort()
triggered_value=int(0.1*len(estimate))
tv=triggered_value
estimate=estimate[tv:len(estimate)-tv]

y=[]
for i in range(len(estimate)):
    y.append(5)

plt.plot(estimate,y,'r--')
plt.plot([statistics.mean(estimate)],[5],'g^')
plt.plot([statistics.median(estimate)],[5],'bo')
plt.plot([5.1],[5],'rs')