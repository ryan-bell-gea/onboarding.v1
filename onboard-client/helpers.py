import requests
import os
import subprocess
import re
import zipfile

def url_response(url):
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/"
    newDir = "Onboarding"
    dirPath = os.path.join(parentPath,newDir)
    if os.path.exists(dirPath) == False:
        os.mkdir(dirPath)
    
    name, url = url
    downPath = os.path.join(parentPath,newDir,name)
    r = requests.get(url, stream = True)
    with open(downPath, 'wb') as f:
        for ch in r:
            f.write(ch)

def java_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/"
    newDir = "Onboarding"
    dirPath = os.path.join(parentPath,newDir)
    os.chdir(dirPath)
    pattern = '\"(\d+\.\d+\.\d+).*\"'

    check = subprocess.run("java -version", capture_output=True, text=True).stderr
    version = re.search(pattern, check).groups()[0]

    if "11.0" not in version:
        #do not uncomment until ready to install
        #subprocess.run("jdk-11_windows-x64_bin.exe /s")
        set_env("JAVA_HOME")
        print("not present")
    if "11.0" in version:
        #do not uncomment until ready to install
        print("Java is present")

def maven_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/Onboarding/"
    newDir = "C:/Program Files/Maven/"
    if os.path.exists(newDir) == False:
        os.mkdir(newDir)
    for x in os.listdir(parentPath):
        if "apache-maven" in x:
            presentDir = os.path.join(parentPath, x)
    with zipfile.ZipFile(presentDir, 'r') as zip_ref:
        zip_ref.extractall(newDir)
    
    check = subprocess.run("mvn -version", capture_output=True, text=True, shell=True).stdout.splitlines()[0]
    if "Apache Maven 3" not in check:
        print("Maven is not present")
        set_env("MAVEN_HOME")
    if "Apache Maven 3" in check:
        print("Maven is present")
        
def git_install():
    username = os.getlogin()
    parentPath = "C:/Users/"+username+"/Downloads/Onboarding/"
    for x in os.listdir(parentPath):
        if "Git-" in x:
            command = x + " /VERYSILENT /NORESTART"
    #subprocess.run(command)
        
        
def set_env(var_name):
    if var_name == "JAVA_HOME": # OPTION: JAVA_HOME
        java_dir = "C:/Program Files/Java/"
        if os.environ.get(var_name) == None: # set JAVA_HOME if it doesn't already exist
            for x in os.listdir(java_dir): # loop through and grab the full path name of jdk directory
                if "jdk-11" in x:
                    target = os.path.join(java_dir, x)
            os.environ[var_name] = target
        elif os.environ.get(var_name) != None:
            print("JAVA_HOME already exists")
            
    elif var_name == "MAVEN_HOME": # OPTION: MAVEN_HOME
        if os.environ.get("JAVA_HOME") == None: # if JAVA_HOME does not exist, create it
            set_env("JAVA_HOME")
        elif os.environ.get("JAVA_HOME") != None: # if JAVA_HOME does exist
            mvn_dir = "C:/Program Files/Maven/"
            if os.environ.get(var_name) == None: # set MAVEN_HOME if it doesn't already exist
                for x in os.listdir(mvn_dir): # loop through and grab the full path name of apache-maven directory
                    if "apache-maven" in x:
                        target = os.path.join(mvn_dir, x)
                os.environ[var_name] = target
            elif os.environ.get(var_name) != None:
                print("MAVEN_HOME already exists")