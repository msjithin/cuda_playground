import os
import numba

os.system("nvcc --version")
print()

print(f'Numba version: {numba.__version__}')
print()

from numba import cuda

cuda.cudadrv.libs.test()
cuda.detect()
print()


import cupyx
print(cupyx.get_runtime_info())

