"""croud computing"""

"""mean by removing 10% i.e. 0.1 of list elements"""

from statistics import mean
estimates=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,3,4,5,6,7,8,6,5,4,2,8,4,3,5,7,3,2,5,7,4,2,5,8,5,1,4,6,8,5,3,1,4,7,8,4,2,5,7]
estimates.sort()
triggered_value=int(0.1*len(estimates))
tv=triggered_value
estimates=estimates[tv:len(estimates)-tv]
print(mean(estimates))

"""mean by removing 10% i.e. 0.1 of list elements using direct formula"""

from scipy import stats
estimate=[1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,3,4,5,6,7,8,6,5,4,2,8,4,3,5,7,3,2,5,7,4,2,5,8,5,1,4,6,8,5,3,1,4,7,8,4,2,5,7]
estimate.sort()
m=stats.trim_mean(estimate,0.1)
print(m)