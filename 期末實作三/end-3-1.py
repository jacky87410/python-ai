import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import math 
import statistics 
from scipy import stats 
import sklearn
import statsmodels.stats.api as sms 
import matplotlib as mpl 
from math import ceil 
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
from IPython.display import display

plt.style.use('seaborn-whitegrid')
font = {'family' : 'Helvetica',
        'weight' : 'bold',
        'size'   : 14}
mpl.rc('font', **font)
effect_size = sms.proportion_effectsize(0.13, 0.15)  
required_n = sms.NormalIndPower().solve_power(
    effect_size, 
    power=0.8, 
    alpha=0.05, 
    ratio=1
    )                                                
required_n = ceil(required_n)                        
print(required_n)
df= pd.read_csv('ab_data.csv')
print(df.head())
print(df.info())
pd.crosstab(df['group'], df['landing_page'])
session_counts = df['user_id'].value_counts(ascending=False)
multi_users = session_counts[session_counts > 1].count()
print(f'There are {multi_users} users that appear multiple times in the dataset')
users_to_drop = session_counts[session_counts > 1].index
df = df[~df['user_id'].isin(users_to_drop)]
print(f'The updated dataset now has {df.shape[0]} entries')
control_sample = df[df['group'] == 'control'].sample(n=required_n, random_state=22)
treatment_sample = df[df['group'] == 'treatment'].sample(n=required_n, random_state=22)
ab_test = pd.concat([control_sample, treatment_sample], axis=0)
ab_test.reset_index(drop=True, inplace=True)
print(ab_test)
print(ab_test.info())
print(ab_test['group'].value_counts())
conversion_rates = ab_test.groupby('group')['converted']
std_p = lambda x: np.std(x, ddof=0)              
se_p = lambda x: stats.sem(x, ddof=0)            
conversion_rates = conversion_rates.agg([np.mean, std_p, se_p])
conversion_rates.columns = ['conversion_rate', 'std_deviation', 'std_error']
print(conversion_rates.style.format('{:.3f}'))
plt.figure(figsize=(8,6))
sns.barplot(x=ab_test['group'], y=ab_test['converted'], ci=False)
plt.ylim(0, 0.17)
plt.title('Conversion rate by group', pad=20)
plt.xlabel('Group', labelpad=15)
plt.ylabel('Converted (proportion)', labelpad=15)
plt.show()
control_results = ab_test[ab_test['group'] == 'control']['converted']
treatment_results = ab_test[ab_test['group'] == 'treatment']['converted']
n_con = control_results.count()
n_treat = treatment_results.count()
successes = [control_results.sum(), treatment_results.sum()]
nobs = [n_con, n_treat]
z_stat, pval = proportions_ztest(successes, nobs=nobs)
(lower_con, lower_treat), (upper_con, upper_treat) = proportion_confint(successes, nobs=nobs, alpha=0.05)
print(f'z statistic: {z_stat:.2f}')
print(f'p-value: {pval:.3f}')
print(f'ci 95% for control group: [{lower_con:.3f}, {upper_con:.3f}]')
print(f'ci 95% for treatment group: [{lower_treat:.3f}, {upper_treat:.3f}]')
#作業：判讀程式最後統計結果，A/B test 是否顯著
#alpha設0.05，p-value = 0.732 P > alpha 因此不能拒絕虛無假設 A = B 
#作業：試以(0.12, 0.11)計算結果是否顯著
#alpha設0.05，p-value = 0.945 P > alpha 因此不顯著 
effect_size = sms.proportion_effectsize(0.12, 0.11)   
required_n = sms.NormalIndPower().solve_power(
    effect_size, 
    power=0.8, 
    alpha=0.05, 
    ratio=1
    )                                                 
required_n = ceil(required_n)                         
print(required_n)
df2 = pd.read_csv('ab_data.csv')
repeat_counts = df2['user_id'].value_counts(ascending=False)
multi_users = repeat_counts[repeat_counts > 1].count()
print(f'There are {multi_users} users that appear multiple times in the dataset')
users_to_drop = repeat_counts[repeat_counts > 1].index
df2 = df2[~df2['user_id'].isin(users_to_drop)]
print(f'The updated dataset now has {df2.shape[0]} entries')
S_control = df2[df2['group'] == 'control'].sample(n=required_n, random_state=22)
S_treatment = df2[df2['group'] == 'treatment'].sample(n=required_n, random_state=22)
ab_test2 = pd.concat([S_control, S_treatment], axis=0)
ab_test2.reset_index(drop=True, inplace=True)
ab_test2['group'].value_counts()
conversion_rates = ab_test2.groupby('group')['converted']
std_p2 = lambda x: np.std(x, ddof=0)   
se_p2 = lambda x: stats.sem(x, ddof=0) 
conversion_rates = conversion_rates.agg([np.mean, std_p2, se_p2])
conversion_rates.columns = ['conversion_rate', 'std_deviation', 'std_error']
print(display(conversion_rates.style.format('{:.3f}')))
plt.figure(figsize=(4,4))
sns.barplot(x=ab_test2['group'], y=ab_test2['converted'], ci=False)
plt.ylim(0.12, 0.1225)
plt.title('Conversion rate by group', pad=20)
plt.xlabel('Group', labelpad=15)
plt.ylabel('Converted (proportion)', labelpad=15)
plt.show()
control_results2 = ab_test2[ab_test2['group'] == 'control']['converted']
treatment_results2 = ab_test2[ab_test2['group'] == 'treatment']['converted']
n_con2 = control_results2.count()
n_treat2 = treatment_results2.count()
successes2 = [control_results2.sum(), treatment_results2.sum()]
nobs2 = [n_con2, n_treat2]
z_stat2, pval2 = proportions_ztest(successes2, nobs=nobs2)
(lower_con2, lower_treat2), (upper_con2, upper_treat2) = proportion_confint(successes2, nobs=nobs2, alpha=0.05)
print(f'z statistic: {z_stat2:.2f}')
print(f'p-value: {pval2:.3f}')
print(f'ci 95% for control group: [{lower_con2:.3f}, {upper_con2:.3f}]')
print(f'ci 95% for treatment group: [{lower_treat2:.3f}, {upper_treat2:.3f}]')
#作業：樣本數是以那些模組/函數算的
#以Ｚ分配做計算