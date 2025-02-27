import os
import json
import time






p = []
def path_to_dic(path):

  


    d = {'name': os.path.basename(path)}
    print("Working on " + os.path.basename(path))
    d['path'] = path
    if os.path.isdir(path):
        d['typ'] = "directory"
       
        d['elemente'] = [path_to_dic(os.path.join(path,sub)) for sub in os.listdir\
    (path)]
    else:
        p.append(path)
    return d

def timeSort(list):
    n = len(list)
    swapped = False
    for i in range(n-1):
        swapped = False
        for j in range(0, n-i-1):
            if(os.path.getmtime(list[j]) > os.path.getmtime(list[j+1])):
                swapped = True
                list[j],list[j+1] = list[j+1],list[j]
        if not swapped:
            return


def mapToTime(list):
    for i in range(len(list)):
        list[i] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(list[i])))


def copyToTime(liste):
    k = []
    
    for i in range(len(liste)):
        k.append((time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(liste[i])))))
    return k


def createDirFromList(list):
    k = []
    for i in range (len(list)):
        ai = {
            "name": os.path.basename(list[i]),
            "path": list[i],
            "modifiedTime": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(list[i]))) }
        k.append(ai)
    
         
    return k



def jsonize(list):
    with open('JSON/lastRecent.json', 'w') as file:
        print(json.dump(list, file,  indent=2))
        print("Successfully completed")


path_to_dic("NotizenDir")
path_to_dic("KlausurenDir")
path_to_dic("FolienDir")
path_to_dic("UebungDir")

timeSort(p)



def run():
    t = copyToTime(p)
    print(p)
    p.reverse()
    print("Trennung p und t")
    print(t)
    ftp = createDirFromList(p)
    print(ftp)



    with open('JSON/recentFiles.json', 'w') as file:
        print(json.dump(ftp,  file,  indent=2))
        print("Successfully completed")