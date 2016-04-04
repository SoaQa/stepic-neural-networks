import numpy as np
print(np.concatenate((np.zeros((3,1)), np.eye(3)), axis=1) + np.eye(3,4)*2)