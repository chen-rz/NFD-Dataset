import numpy as np
import matplotlib.pyplot as plt

data = np.load('./NFD.npy', allow_pickle=True)
data = dict(data.item())

fig, axs = plt.subplots(10, 20, figsize=(10, 10))

for i in range(10):
    for j in range(20):
        img_array = data['train_images'][i*10 + int(j / 2)][j % 2]
        axs[i, j].imshow(img_array, cmap='gray')
        axs[i, j].axis('off')
        axs[i, j].set_title(str(i*10 + int(j / 2) + 1) + ('A' if j % 2 == 0 else 'B') + '[{}]'.format(data['train_labels'][i*10 + int(j / 2)]))

plt.tight_layout()
plt.show()
