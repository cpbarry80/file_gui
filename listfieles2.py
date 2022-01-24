import os.path, time
import os
from fuzzy_match import match
from fuzzy_match import algorithims

def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

curnames = []
directory= "C:\Models\Cedar Rapids\CURRENT MODEL\Work"
for i in absoluteFilePaths(directory):
    filesname_raw = os.path.split(i)[-1]
    filesname_clean = ''.join([i for i in filesname_raw if not i.isdigit()]).lower().replace(" ", "")
    curnames.append(filesname_clean)


directory= "C:\Models\Cedar Rapids\OLD MODEL\Work"
threshold = 0
for i in absoluteFilePaths(directory):
    filesname_raw = os.path.split(i)[-1]
    filesname_clean = ''.join([i for i in filesname_raw if not i.isdigit()]).lower().replace(" ", "")
    #dont go into subdirectories
    #ignore file extension (csv vs. xls)
    for curname in curnames:
        listofmatchesidk = algorithims.trigram(filesname_clean, curname)
        if listofmatchesidk < 0.8:
            print(listofmatchesidk, filesname_clean, curname)
            continue
    lastmodified= time.ctime(os.path.getmtime(i))
    createddate = time.ctime(os.path.getctime(i))









