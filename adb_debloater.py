#!/usr/bin/python3
from subprocess import Popen, check_output, PIPE, STDOUT
import time

path = '/home/aerial/Downloads/platform-tools/adb'              ## Path to adb file
prgrm_list = open("program_list.txt","r").read().split('\n')    ## Open the file program_list.txt, list of all programs to remove

try:
    check_output([path,'get-state']).decode('UTF-8')            ## Check if device connected 
except:
    print("Connect a device first.")                            ## If not abort and print..
else:
    for line in prgrm_list:                                     ## For every program listed in program_list.txt
        rm_line = 'pm uninstall -k --user 0 ' + line            ## Line to run in shell
        try:
            result = Popen([path,'shell'], stdout=PIPE, stdin=PIPE, stderr=PIPE)    ## Open shell on phone
            data = result.communicate(input=rm_line.encode())                       ## Set data to what adb shell returns when rm_line is run
            time.sleep(0.5)                                                         ## Sleep/Pause for 0.5 seconds
        except Exception as e:
            print("An error occured:")                                              
            print(e)                                                                ## Print error
        else:
            print(line,':',data[0].decode('UTF-8').replace('\n',''))                ## Print program that is removed and data[0] (what adb shell 
                                                                                    ## command returns)