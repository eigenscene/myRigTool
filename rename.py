import pymel.core as pm

selCom = pm.ls(selection = True, flatten = True, objectsOnly = True)

for selComThis in selCom:
    selComSplit = selComThis.longName().split('|')[1:] 
    updatedName = ''
    for selComSplitThis in selComSplit[:-1]:
        updatedName += selComSplitThis + '|'
    updatedName += 'robot_' + selComSplit[-1]
    selComThis.rename(updatedName)

#for i in selCom:
#    print i
#    updatedName = 'robot_' + i
#    print updatedName
#    i.rename(updatedName)