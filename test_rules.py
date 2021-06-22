import glob
import sys
import os
import RCpyGHDL
import logging
import subprocess

def AnalyzeFile(fichier):
   print('INFO:Analyze ',  fichier)
   Rule = RCpyGHDL.RCpyGHDL("--std=08",fichier)
   print("INFO: Rule CNE_02500 : list all entity ports")
   Rule.CNE_02500()
   print("INFO: Rule CNE_02600 : list all signals")
   Rule.CNE_02600()
   print("----------------") 
   os._exit(0)  



def AnalyzeAllFiles():
    #list all vhd file
    listfiles=glob.glob("*.vhd")
    print(listfiles)


    #apply rules on files
    for fichier in listfiles:
        print(fichier)
        try:
            newpid = os.fork()
            if newpid == 0:
                #fork to execute analysis (this is the only solution to avoid program crash due to libghdl scann error)
                AnalyzeFile(fichier)
            else:
                os.waitpid(newpid, 0)  # wait for fork to finish
        except:
            print("ERROR: Analysing "+fichier)    
            pass

#prepare log need tee on linux
logfile = "analysis.log"
tee = subprocess.Popen(["tee", logfile], stdin=subprocess.PIPE)
# Cause tee's stdin to get a copy of our stdin/stdout (as well as that of any
# child processes we spawn).
os.dup2(tee.stdin.fileno(), sys.stdout.fileno())
os.dup2(tee.stdin.fileno(), sys.stderr.fileno())

#launch analysis
AnalyzeAllFiles()