# get your laptop organized
#1 collect all python modules 


dst = '/Users/J/Scripts_python'
import os, glob
import shutil
os.chdir('/Users/J')
for file in glob.glob('*.py'):
    print(file)
    shutil.copy2(file, dst)
    
    
    
    
#2 collect all photos 


dst = '/Users/J/Photo'
import os, glob
import shutil
os.chdir('/Users/J')
for file in glob.glob('*.jpeg'):
    print(file)
    shutil.copy2(file, dst)
    
   
    


