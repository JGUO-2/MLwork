# -*- coding: utf-8 -*-
"""
  按照常见概率分布生成数字
   计算相应统计量
"""
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

"""
  正态分布
"""

normal_value = []
for _ in range(1000):         # 产生一组满足标准正态分布的随机数
    normal_value.append(random.normalvariate(0, 1))
plt.hist(normal_value, bins=30)       # bins直方图的柱数
plt.show()
normal_mean = np.mean(normal_value)
normal_var = np.var(normal_value,ddof = 1)
normal_std = np.std(normal_value, ddof = 1 )
normal_dis = np.max(normal_value)-np.min(normal_value)
normal_mid = np.median(normal_value)
print("**********标准正态分布***********")
print('生成的随机数列表为',normal_value)
print('样本均值为：',normal_mean)
print('样本方差为：',normal_var)
print('样本标准差为：',normal_std)
print('样本极差为：',normal_dis)
print('样本中位数为：',normal_mid)

"""
二项分布
"""

bin_sample = np.random.binomial(50,0.5,size=1000)      # 50次试验，事件发生概率为0.5，产生1000个符合二项分布的随机数
bins = np.arange(50)
plt.hist(bin_sample, bins=bins, align='left', density=True, rwidth=0.1)  # 绘制直方图
plt.title('Binomial PMF with n=50, p=0.05')   #设置标题和坐标
plt.xlabel('number of successes')
plt.ylabel('probability')
plt.show()
bin_mean = np.mean(bin_sample)
bin_var = np.var(bin_sample)
bin_std = np.std(bin_sample)

print("**********二项分布***********")
print('生成的随机数列表为',bin_sample)
print('样本均值为：',bin_mean)
print('样本方差为：',bin_var)
print('样本标准差为：',bin_std)



"""
  泊松分布
"""

# 设置random_state时，每次生成的随机数一样。不设置或为None时，多次生成的随机数不一样
poisson_sample = stats.poisson.rvs(mu=5, size=100, random_state=3)

bins = np.arange(20)
plt.hist(poisson_sample, bins=bins, align='left', rwidth=0.1, density=True)     # 绘制直方图
plt.title('Poisson PMF ')                  # 设置标题和坐标轴
plt.xlabel('number of arrivals')
plt.ylabel('probability')
plt.show()
poisson_mean = poisson_sample.mean()
poisson_var = poisson_sample.var()
poisson_std = poisson_sample.std()
poisson_dis = poisson_sample.max()-poisson_sample.min()
print("**********泊松分布***********")
print('生成的随机数列表为',poisson_sample)
print('样本均值为：',poisson_mean)
print('样本方差为：',poisson_var)
print('样本标准差为：',poisson_std)
print('样本极差为：',poisson_dis)


"""
  指数分布
"""
tau = 10
exp_sample = np.random.exponential(tau, size = 1000)              # 产生1000个满足指数分布的随机数
plt.hist(exp_sample, bins = 80, alpha = 0.6, density = True)     # 绘制直方图
plt.margins(0.02)

# 绘制指数分布的概率密度函数
lam = 1 / tau
x = np.arange(0,80,0.1)
y = lam * np.exp(- lam * x)
plt.plot(x,y,color='blue', lw=3)
plt.title('Exponential distribution')               #设置标题和坐标轴
plt.xlabel('time')
plt.ylabel('PDF')
plt.show()

exp_mean = exp_sample.mean()
exp_var = exp_sample.var()
exp_std = exp_sample.std()
exp_dis = exp_sample.max()-exp_sample.min()
print("**********指数分布分布***********")
print('生成的随机数列表为',exp_sample)
print('样本均值为：',exp_mean)
print('样本方差为：',exp_var)
print('样本标准差为：',exp_std)
print('样本极差为：',exp_dis)


