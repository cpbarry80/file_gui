
import os
from fuzzy_match import algorithims
import pandas as pd


def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

def cleanfile(file):
    return ''.join([i for i in file if not i.isdigit()]).lower().replace(" ", "").replace(".", "").replace("_", "")


def files_potentially_missing(oldmodelpath, curmodelpath):
    problems = []
    for old_file_name in files(oldmodelpath):
        oldoriginalfilenamenoextension = os.path.splitext(old_file_name)[0]
        oldfilesname_clean = cleanfile(oldoriginalfilenamenoextension)
        scores = {}
        for originalfilename in files(curmodelpath):
            originalfilenamenoextension = os.path.splitext(originalfilename)[0]
            filesname_clean = cleanfile(originalfilenamenoextension)
            listofmatchesidk = algorithims.trigram(oldfilesname_clean, filesname_clean)
            scores.update({listofmatchesidk : [originalfilename, filesname_clean]})
        all_values = scores.keys()
        max_value = max(all_values)
        problems.append([old_file_name, str(round(max_value, 2)), scores[max(all_values)][0]])
    ovn = pd.DataFrame(problems, columns = ['old model file', 'match_score', 'new model file']).sort_values(by=['match_score'])
    ovn.set_index('match_score')
    return ovn


oldmodelpath = "C:\Models\Cedar Rapids\OLD MODEL\Work"
curmodelpath = "C:\Models\Cedar Rapids\CURRENT MODEL\Work"
ovn = files_potentially_missing(oldmodelpath, curmodelpath)
print(ovn)

