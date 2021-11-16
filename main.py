import pandas as pd

df = pd.read_csv("marketing_data.csv")
# cluster sampling
df['cluster'] = pd.cut(df['ID'], bins=10, labels=False) + 1
df.to_csv('marketing_data_cluster_sampling.csv', index=False)
print(df)
# simple random sampling
simple_random_sample = df.sample(n=10).sort_values(by='ID')
print(simple_random_sample)
