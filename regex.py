# %%
#ex
import pandas as pd
import numpy as np
import re
import os
import shutil
import glob as glob
import datetime as dt

# %%
os.getcwd()

# %%
os.listdir(r'C:\Users\PC\Desktop\cosas')
#os.stat(r'C:\Users\PC\Desktop\cosas HSBC')

# %%
files = glob.glob(r'C:\Users\PC\Desktop\cosas\*')

for i in files:
    print(dt.datetime.fromtimestamp(os.path.getmtime(i)))
    
# %%
def newest(path):
    times = []
    files = os.listdir(path)
    paths = [os.path.join(path, basename) for basename in files]
    for i in paths:
        times.append(os.path.getctime(i))
    return times

# %%
path = r'C:\Users\PC\Desktop\cosas'
newest(path)

# %%
#agarrar archivos creados hoy en x carpeta

def created_today(path):
    today = dt.datetime.today()
    day = dt.timedelta(days=1)
    files = os.listdir(path)
    files_created_today = []
    full_path = [os.path.join(path, basename) for basename in files]
    for i in full_path:
        if dt.datetime.fromtimestamp(os.path.getctime(i)) > today-day:
            files_created_today.append(i)
        else:
            None
    return files_created_today
    
# %%
s = created_today(r'C:\Users\PC\Desktop\cosas')

# %%
s

# %%
#mover/copiar archivos creados en los ult 15 minutos en x carpeta

def created_today(path):
    today = dt.datetime.today()
    dif = dt.timedelta(minutes=15)
    files = os.listdir(path)
    files_created_today = []
    full_path = [os.path.join(path, basename) for basename in files]
    for i in full_path:
        if dt.datetime.fromtimestamp(os.path.getctime(i)) >= today-dif:
            shutil.copy2(i, r'F:\CV')
            #shutil.copy2(i, r'F:\CV\lawea.txt')
            #shutil.move(i, r'C:\Users\PC\Desktop\mover aca')
            #os.rename(i, r'F:\CV\texto_nuevo.txt')
        else:
            None
# %%
created_today(r'C:\Users\PC\Desktop\cosas HSBC')

# %%
#os.getcwd()
df = pd.read_csv(r'C:\Users\PC\Desktop\test_regex.txt', header=None)

# %%
df

# %%
regexp = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
df[0].apply(lambda x: x if regexp.search(x) else None)


# %%
mystring = 'Here is  some   text   I      wrote   '

# %%
mystring.split()

# %%
' '.join(mystring.split())
# %%
import re
str = "Albuquerque is my     turkey and he's   feathered and    he's      fine, And    he"
print (re.sub(r' +', ' ', str))
# %%
