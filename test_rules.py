import glob
import sys
#sys.path.append(".")
import RCpyGHDL

#list all vhd file
listfiles=glob.glob("*.vhd")
print(listfiles)

#apply rules on files
for fichier in listfiles:
    print(fichier)
    try:
        Rule = RCpyGHDL.RCpyGHDL("--std=08",fichier)
        print("INFO: Rule CNE_02500 : list all entity ports")
        Rule.CNE_02500()
        print("INFO: Rule CNE_02600 : list all signals")
        Rule.CNE_02600()
        print("----------------")
    finally:
        pass