import numpy as np
import pickle as pkl
import seaborn as sns
import matplotlib.pyplot as plt

CB_color_cycle = ['#377eb8', '#ff7f00', '#4daf4a',
                  '#f781bf', '#a65628', '#984ea3',
                  '#999999', '#e41a1c', '#dede00']
sns.set_style("whitegrid")
save_path = './result.png'
paths=['/home/ofir/code/traj_info_local_access/experiments/latip_long_lava_2023-04-19/14-29-54/seed_0/info.pkl',
       '/home/ofir/code/traj_info_local_access/experiments/tip_long_lava_2023-04-17/13-06-49/seed_0/info.pkl']
labels =['latip','tip']

plt.figure()

for i, path in enumerate(paths):
    with open(path, "rb") as f:
        info = pkl.load(f)
    y = np.array(info['Eval Returns'])
    x = np.array(info['Eval ndata'])
    y_mean = y.mean(-1)
    y_std = y.std(-1)
    plt.plot(x,y_mean,label=labels[i])
    plt.fill_between(x, y_mean + y_std, y_mean - y_std, alpha=0.1)

plt.legend(loc='upper left', fontsize=10)
plt.savefig(save_path)