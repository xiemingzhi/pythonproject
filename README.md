# pythonproject
Common Python scripts 

Requirements:
* Python 3.7 
* pip install requests
* pip install json
* anaconda 

Some scripts have different requirements see: [scripts/README.md](scripts/README.md)

Create environment
```
conda env create -f environment.yml
conda activate pythonproject
```

Add packages 
```
conda install modulename
conda install sortedcontainers
```

Export environment
```
conda env export -f environment.yml
```

Update environment
```
conda env update -f environment.yml
```

**To Run**

python filename.py

## vscode

Install microsoft python extension
```
select python interpreter (use pythonproject conda environment)
select windows command prompt for terminal
select py file 
ctrl+shift+p select 'Run Pythin File in Terminal' command
```

