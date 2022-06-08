Extending module load path

There are a couple of ways to tell the Python interpreter where to look for modules, aside from the default local directory and built-in modules. You can use the environment variable PYTHONPATH to specify additional directories to look for modules like this:

PYTHONPATH=/foo python game.py

This executes game.py, and enables the script to load modules from the foo directory, as well as the local directory.

You may also use the sys.path.append function. Execute it before running the import command:

sys.path.append("/foo")

Now the foo directory has been added to the list of paths where modules are looked for.