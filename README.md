# RCpyGHDL
This is a collection a functions to evaluate VHDL Rules using Python libGHDL.

## Installation
* Install libghdl and GHDL python library:    
      To install libghdl you have to compile ghdl getting the sources from https://github.com/ghdl/ghdl and follow the installation from https://ghdl.github.io/ghdl/development/building/index.html   
      *Note* : I do recommand to install GHDL outside the PATH (like /opt/GHDL) otherwise it can break GCC.
* Install Python pyGHDL:  
      pyGHDL is currently under heavy development. To install it run `pip install .` in ghdl source folder
* Configure the new PATH to register ghdl   

      
      PATH=/opt/ghdl/bin/:$PATH   
      export LD_LIBRARY_PATH=/opt/ghdl/lib:$LD_LIBRARY_PATH   
      
      
## Test
Simply put any VHDL files in the folder and run `python test_rules.py`

## Development 
Developping under libGHDL is quite difficult here are some tips:

1. Use AST from your VHDL file to know what you are looking for: use command `ghdl -a -dp my_file.vhd &> my_file_ast.txt` to generate it
Here is an example of it. (Be careful Types are written in lowercase for every first word and in python you have to use uppercase for first letter)

2. Get the GHDL source code:
      1. Folder `ghdl-master\pyGHDL\libghdl` : provides source code for the python binding to libghl
         `ghdl-master\pyGHDL\libghdl\vhdl\nodes.py`: provides type definition and node functions
         `ghdl-master\pyGHDL\libghdl\vhdl\nodes_meta.py`: provides check and specific access to nodes fields 
         `ghdl-master\pyGHDL\libghdl\utils.py`:provides more pythonic access to elements (still under development)
      2. Folder `ghdl-master\src\vhdl` :   
          We've got ads files which are functions prototypes and adb which are the function source code   
          For the above python source you've got the ada source code : `vhdl-nodes.ads / vhdl-nodes.adb` , `vhdl-nodes_meta.ads / vhdl-nodes_meta.adb`   
      3. File `ghdl-master\src\vhdlvhdl-disp_tree.ad[sb]`  is of great use to get access to elements   
      4. see ghdl-master\ghdl-master\doc\internals\AST.rst for docuemntation about the AST   
