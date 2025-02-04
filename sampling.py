import pandas as pd
df = pd.read_csv('labeled_data.csv')
sampled_df = df.sample(frac=0.1, random_state=42)
sampled_df.to_csv('short_labeled_data.csv', index=False)

