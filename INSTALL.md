# Set up the environment


## 1. Sign up for an IBM Quantum account

Instructions can be found at the [Qiskit IBM Runtime](https://github.com/Qiskit/qiskit-ibm-runtime/tree/stable/0.4#qiskit-runtime-on-ibm-quantum) repository.

## 2. Clone this repository

We assume that [git](https://git-scm.com/) is installed.  As a first step, clone the repository and enter the clone's directory:

```sh
$ git clone https://github.com/mberna/ieee-qce22-qiskit-runtime-primitives-tutorial.git
$ cd ieee-qce22-qiskit-runtime-primitives-tutorial
```

The remainder of this document will assume you are in the root directory of the repository.

## 3. Set up a virtual Python Environment

Next, we assume that [Python](https://www.python.org/) 3.8 or higher is installed.  It is recommended to use a Python virtual environment that is dedicated to working with this repo.  The steps in the remainder of this document will assume that this environment is activated using either method.

### Option 1: venv (included in Python)

You can create and activate a virtual environment with the following commands:

```sh
$ python3 -m venv venv
$ source venv/bin/activate
```

The first command creates a virtual environment in the `venv` folder of the current directory.  We recommend using this name, as it will be ignored by git (i.e., we have added it to `.gitignore`).

Any time you open a new shell and wish to work with this repo, you will need to activate it using the second line above.  (If you prefer that the virtual environment be activated automatically any time you enter the directory, you may wish to look into using [direnv](https://direnv.net/) or a similar tool.)

### Option 2: conda (recommended only if it is your tool of choice)

The following commands create and activate a conda virtual environment named `qiskit_runtime_env`:

```sh
$ conda create -n qiskit_runtime_env python=3.8
$ conda activate qiskit_runtime_env
```

Any time you open a new shell and wish to work with this repo, you will need to activate it using the second line above.


## 4. Install the packages

All of the packages needed for this tutorial can be installed by running:

```
$ pip install -r requirements.txt
```

## 5. Verify your installation

Run the [`hello_world.py`](docs/hello_world.py) script to verify your installation:

```shell script
$ python3 ./hello_world.py
```

This script will prompt you for your IBM Quantum token, unless you had previously saved it on disk.
Once finished, the script will print `Hello, World!`. It may take a minute or two for the script to complete.

## 6. Using Jupyter Notebooks

Jupyter should already be installed into the virtual environment if you ran the command in the previous step.

Then, start the notebook server.  From the root directory:

```sh
$ jupyter notebook
```

Make sure the notebook server is started from the same Python environment (venv or conda) from which you ran `pip install -r requirements.txt`; otherwise, it may not find this repo in the path.

Once the notebook server starts, it will provide a URL for accessing it through your web browser.  The tutorial notebooks can be found in the [docs directory](docs/tutorials/README.md).
