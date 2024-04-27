import cudf
from cuml.cluster import DBSCAN
import os

import numba

os.system("nvcc --version")
print()

print(numba.__version__)
print()

from numba import cuda

cuda.cudadrv.libs.test()
cuda.detect()
print()

# Create and populate a GPU DataFrame
gdf_float = cudf.DataFrame()
gdf_float['0'] = [1.0, 2.0, 5.0]
gdf_float['1'] = [4.0, 2.0, 1.0]
gdf_float['2'] = [4.0, 2.0, 1.0]

# Setup and fit clusters
dbscan_float = DBSCAN(eps=1.0, min_samples=1)
dbscan_float.fit(gdf_float)
print()
print(dbscan_float.labels_)

import cupyx
print()
print(cupyx.get_runtime_info())

