import numpy as np

import utils
from quaternion import quaternion_product, quaternion_to_rotation_matrix, quaternion_to_euler, euler_to_quaternion

q_a = euler_to_quaternion(np.array([0.2, 0.1, 0]))
# q_b = euler_to_quaternion(np.array([0, 4, 0]))

# prod = quaternion_product(q_a, q_b)

eul_a = quaternion_to_euler(q_a)
print(eul_a)
