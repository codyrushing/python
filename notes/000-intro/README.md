## Virtual environments
Basically does what node does by default, but does it in a self-contained folder that creates a sort of self-contained python installation
```bash
$ mkdir pyworkshop
$ cd pyworkshop
$ python3.7 -m venv env
$ source env/bin/activate
```
This makes a virtual env in the `env` folder.  `source env/bin/activate` activates the virtual env, which is indicated by the `(env)` prefix in the command line.