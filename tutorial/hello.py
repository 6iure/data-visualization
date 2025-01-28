# %%
import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline ?
import seaborn as sns
print("Setup Complete")

# %%
fifa_path = '/home/iure/work/data-visualization/data/fifa.csv'

fifa_data = pd.read_csv(fifa_path, index_col="Date", parse_dates=True)


# %%
fifa_data.head()

# %%

# indica o tamanho e largura da figura 
plt.figure(figsize=(16, 6))

#cria um grafico que mostra como os rankings da fifa evoluiram com o tempo
sns.lineplot(data=fifa_data)
# %%
