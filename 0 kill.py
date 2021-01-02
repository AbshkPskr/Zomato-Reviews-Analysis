# import os, signal 
   
# def process(): 
      
#     # Ask user for the name of process 
#     name = input("Enter process Name: ") 
#     try: 
#         # iterating through each instance of the proess 
#         while True:
#             for line in os.popen("ps ax | grep " + name + " | grep -v grep"):  
#                 fields = line.split() 
                
#                 # extracting Process ID from the output 
#                 pid = fields[0]  
                
#                 # terminating process  
#                 os.kill(int(pid), signal.SIGKILL)  
#             print("Process Successfully terminated") 
            
          
#     except: 
#         print("Error Encountered while running script") 
   
# process()

import psutil

# while True:
for proc in psutil.process_iter():
    if str(proc.name()) == 'chrome.exe':
        proc.kill()
        print("----------------------------------")
        # dic = proc.as_dict()
        # for key in dic:
        #     print(str(key)+"----------------"+str(dic[key]))
        # break
