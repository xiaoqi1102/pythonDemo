#-*-coding:utf-8-*-
from __future__ import division
import pandas as pd
import numpy as np
from scipy import stats

##0.read Data ##
df = pd.read_csv("./data/train.csv")
label = df['TARGET']
df = df.drop(['ID', 'TARGET'], axis=1)

missSet = [np.nan, 9999999999, -999999]
print('missSet:\n', missSet)
len(df.iloc[:,0].unique())

count_un = df.iloc[:,0:3].apply(lambda x:len(x.unique()))
df.iloc[:,0:3].head(5)
print('count_un:\n', count_un)
np.sum(df.iloc[:,0] == 0)

count_zero = df.iloc[:,0:3].apply(lambda x:np.sum(x == 0))
print('count_zero:\n', count_zero)

np.mean(df.iloc[:,0:3])
df.iloc[:,0][~np.isin(df.iloc[:,0], missSet)]
df_mean = df.iloc[:, 0: 3]
df_mean = df.iloc[:,0:3].apply(lambda x:np.mean(x[~np.isin(x,missSet)]))
print('df_mean:\n', df_mean)
df_median = df.iloc[:,0:3].apply(lambda x:np.median(x[~np.isin(x,missSet)]))
print('df_median:\n', df_median)
df_mode = df.iloc[:,0:3].apply(lambda x: stats.mode(x[~np.isin(x,missSet)])[0][0])
print('df_mode:\n',df_mode)
# 众数频数
df_mode_count = df.iloc[:, 0: 3].apply(lambda x: stats.mode(x[~np.isin(x, missSet)])[1][0])
print('df_mode_count:', df_mode_count)
# df.shape[0] 取的是行  df.shape[1]取的是列
df_mode_perct = df_mode_count/df.shape[0]
print('df_mode_perct:', df_mode_perct)

df_min = df.iloc[:, 0: 3].apply(lambda x: np.min(x[~np.isin(x, missSet)]))
print('df_min', df_min)
df_max = df.iloc[:,0:3].apply(lambda x: np.max(x[~np.isin(x, missSet)]))
print('df_max', df_max)

json_quantile = {}
for i, name in enumerate(df.iloc[:,0:3].columns):
    # print('the {} columns: {}').format(i, name)
    json_quantile[name] = np.percentile(df[name][~np.isin(df[name], missSet)] , (1, 5, 25, 50, 75, 95, 99))
print('json_quantile:', json_quantile)
df_quantile = pd.DataFrame(json_quantile)[df.iloc[:,0:3].columns].T
print('df_quantile:', df_quantile)

json_fire_name = {}
json_fire_count = {}
def fill_fire_top_5(x):
    if(len(x)) <= 5:
        new_array = np.full(5, np.nan)
        new_array[0:len(x)] = x
        return new_array
for i, name in enumerate(df[['ind_var1_0', 'imp_sal_var16_ult1']].columns):
    index_name = df[name][~np.isin(df[name], missSet)].value_counts().iloc[0:5, ].index.values
    index_name = fill_fire_top_5(index_name)
    json_fire_name[name] = index_name
    values_count = df[name][~np.isin(df[name], missSet)].value_counts().iloc[0:5,].values
    values_count = fill_fire_top_5(values_count)
    json_fire_count[name] = values_count
print('json_fire_count:', json_fire_count)
print('json_fire_name:', json_fire_name)
df_fre_name = pd.DataFrame(json_fire_name)[df[['ind_var1_0', 'imp_sal_var16_ult1']].columns].T
df_fre_count = pd.DataFrame(json_fire_count)[df[['ind_var1_0', 'imp_sal_var16_ult1']].columns].T
print('df_fre_name:', df_fre_name)
print('df_fre_count:', df_fre_count)
df_fre = pd.concat([df_fre_name, df_fre_count], axis = 1)
print('df_fre:', df_fre)