""" Author: DaveTheBomb
    Date:   June 2020
"""

import os
import subprocess

def compile_prgram():
    """
    This function compiles the program and creates an exe file
    """
    compiler = input("Default compiler = 'g++' \nPress Enter-key to continue\n")
    filename = ""
    c = 'N'
    while(c != 'Y'):
        file = input("Ënter the file to be compiled and press Enter-key (include file extention).\n")
        if os.path.isfile(file):                    
            filename += file + " ";
        else:
            print("%s does not exist on the current directory" %file)
        c = input("Have you entered all the files needed (Y/N)?\t")
        
    cmd = "g++ " + filename + "-o new"
    try:
        failure =  subprocess.check_call(cmd, shell = True, stderr = subprocess.STDOUT)
    except subprocess.CalledProcessError:
        print("\nProgram failed to compile:\nPossible issues:\n\t* Compiler\n\t* Source file(s)")
        return [False, '']
    return [True, 'new.exe']


def run_executable(exe_file):    
    """
    This program automates the process of running a program and gives it
    the inputs if required. The input is stored in a textfile called input.txt
    """    
    finput  =  open('input.txt', 'r')
    foutput = open('output.txt', 'w')
    p = subprocess.Popen(exe_file, stdin = finput, stdout = foutput)
    p.wait()
    foutput.flush()
    foutput.close()
    finput.close()
    os.remove('new.exe')
    return
    

def main():
    
    [compile_status, exe_file] = compile_prgram()
    if(compile_status):
        run_executable(exe_file)
        print("\nProgram succeful!")
    else:
        print("\nProgram NOT succeful!")

    # pauses the console window.
    stop = input()
    return

main()




    
