import pandas as pd

# imoprt zombie training dataset
zombie_df = pd.read_csv('training.csv')

X = zombie_df.drop(columns=['bite_size','green_blood_count','infected_family','location'])
y = zombie_df['is_zombie']

print(X)


