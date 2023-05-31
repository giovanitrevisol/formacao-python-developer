# venv

## Creating a virtual environment

If you use the PyCharm IDE, automatically when you create a projet a venv folder will be created.

**Procedure Manually**
```shell
mkdir new_project
```
```shell
cd new_project
```

**create venv**
```shell
python3 -m venv name_virtual_environment
```

But, it is not enough just to create environment, it is necessary to activate it:
```shell
source name_virtual_environment/bin/activate
```

## Replicating environment

### export dependencies
```shell
pip freeeze > requirements.txt
```
With the above command, a file will be created with all the libraries present in our virtual environment.

Ok...

Now, if we want to run our project on another machine, it not wants to download the dependencies one by one, just do:
```shell
pip install -r requirements.txt  
```
With command, all libraries present in the requirement.txt will be automatically installed.

### Disable the virtual environment:
```shell
deactivate
```