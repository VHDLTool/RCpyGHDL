# RCpyGHDL
This is a collection a functions to evaluate VHDL Rules using Python libGHDL.

## Installation
* Install libghdl and GHDL python library:    
      To install libghdl you have to compile ghdl getting the sources from https://github.com/ghdl/ghdl and follow the installation from https://ghdl.github.io/ghdl/development/building/index.html   
      *Note* : I do recommand to install GHDL outside the PATH (like /opt/GHDL) otherwise it can break GCC.
* Install Python pyGHDL:  
      pyGHDL is currently under heavy development. To install it run `pip install .` in ghdl source folder
* Configure the new PATH to register ghdl   
      ```
      PATH=/opt/ghdl/bin/:$PATH   
      export LD_LIBRARY_PATH=/opt/ghdl/lib:$LD_LIBRARY_PATH
      ``` 
      
## Test
Simply put any VHDL files in the folder and run `python test_rules.py`

##Development 
Developping under libGHDL is quite difficult here are some tips.

1.Use AST from your VHDL file to know what you are looking for: use command `ghdl -a -dp my_file.vhd &> my_file_ast.txt` to generate it
Here is an example of it. (Be careful 
