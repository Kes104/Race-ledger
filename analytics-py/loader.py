import pandas as pd
import numpy as np

df = pd.read_csv('Silverstone.csv')
df = df.rename(columns={'# x_m': 'x_m'})

# gap between each point and the previous one (first row is NaN, dropped)
gaps = np.sqrt(df['x_m'].diff()**2 + df['y_m'].diff()**2).dropna()

# closing gap: last point back to first
closing = np.hypot(df['x_m'].iloc[0] - df['x_m'].iloc[-1],
                   df['y_m'].iloc[0] - df['y_m'].iloc[-1])

print(f"gaps  min={gaps.min():.2f}  max={gaps.max():.2f}  mean={gaps.mean():.2f}")
print(f"closing gap = {closing:.2f} m")
print(f"lap length  = {(gaps.sum() + closing)/1000:.3f} km")