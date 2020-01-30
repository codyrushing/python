I am using `pyenv` to manage the python version on a per-project level.  Works like `nvm`.
* `pyenv install $VERSION`
* It creates a `.python-version` file in the project which indicates the python version.

Python 3 ships with `venv` which is a built-in tool for creating virtual environments.  Here's how to use it
* `cd` into the project root
* run `python -m venv env` to create a virtual environment in the `/env` directory (not unlike node_modules)
  * the `-m` command line argument tells python to run it as a script.  I'm not really sure what this means, but it sounds like it has something to do with resolving relative file imports, see more explanation here [https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not](https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not)
  * after creating the virtual environment, you can activate it by running `env/bin/activate`