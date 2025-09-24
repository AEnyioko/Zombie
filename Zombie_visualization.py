import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# imoprt zombie training dataset
zombie_df = pd.read_csv('training.csv')

x = zombie_df.drop(columns=['bite_size','green_blood_count','infected_family','location'])
y = zombie_df['is_zombie']

sns.histplot(zombie_df, x='bite_size', hue='is_zombie', kde=True)
plt.title('Distribution of Bite Size by Zombie Status')
plt.show()