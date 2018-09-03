import numpy as np
import matplotlib.pyplot as plt

vector1 = [0, 0.3, 1, 1.65, 1.98, 2.68, 3, 4.9, 5, 6]
teste1 = np.array(vector1)
print(teste1)

plt.hist(teste1)
plt.show()
plt.clf()

plt.hist(teste1, bins = 20)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('População Mundial')
plt.yticks([0, 2, 3, 4])
plt.xticks["1b", "2b", "3b", "4b", "5b", "6b"]
plt.show()