# Cuda playground

This repo deals with setting up cuda, testing it and exploring GPU driven data analysis.

Source:
https://www.golinuxcloud.com/install-cuda-on-ubuntu/

Source   
https://github.com/rapidsai/cuml

## Creating a Virtual Environment
Begin by creating a virtual environment to isolate your project dependencies. Open a terminal and run the following command:
```
python -m venv .venv
```
Replace .venv with your desired virtual environment name.

Activate the virtual environment by running the following command:
```
source .venv/bin/activate
```

## Test if cuda is working
```
python cuda_test.py
```

## Installing Jupyter and IPykernel
```
pip install ipykernel jupyter
```
## Creating a CUDA Kernel for Jupyter

We need to create a Jupyter kernel that uses CUDA. Execute the following command:
```
python -m ipykernel install --user --name=cuda --display-name "cuda-gpt"
```
Here, --name specifies the virtual environment name, and --display-name sets the name you want to display in Jupyter Notebooks.

## Using the CUDA Kernel in Jupyter Notebooks

First open the jupyter notebook server:
```
jupyter notebook
```
Open Jupyter Notebooks . Create or open a notebook and select “Change Kernel” from the menu. Choose “Jupyter” and then select the newly created “cuda-gpt” kernel.

Or if you want to setup cuda kernel environment in vscode you can click on 'Serlect Kernel' on top right on teh notebook, select 'Existing Jupyter server' and enter the jupyter server url.


