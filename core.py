# -----------------------------------------------------------------------------------
# Created by ken Feb 26 2016
# Modified by ken Feb 27 2016
# Copyright (c) 2016 ken. All rights reserved.

# Description:
#    This is a tool to make rigging easier.
#        - Align controller position and orientation with joint.
#        - Rename controller to 'JOINT_NAME_ctrl'.

# How to run:
#     - Copy this script to "\C:\Users\USER_NAME\Documents\Maya\MAYA_VERSION\scripts".
#     - Type ""
# -----------------------------------------------------------------------------------
# import modules
# -----------------------------------------------------------------------------------

import pymel.core as pm

# -----------------------------------------------------------------------------------
# check if last selection is joint.
# -----------------------------------------------------------------------------------

def checkSelection(selCom):
    print selCom[-1]
    if len(selCom) < 2:
        pm.error('Please select a controller and joint')
    if not pm.objectType(selCom[-1], isType='joint'):
        pm.error('Please select a joint for last')

# -----------------------------------------------------------------------------------
# Align orientation of controller with selected joint.
# Achieves this by doing the following.
#   - group controller
#   - parent group to joint
#   - set group translation and rotation to zero
#   - unparent
#   - ungroup
# -----------------------------------------------------------------------------------

def alignCtrlToJnt():
    selCom = pm.ls(sl = True, fl = True)
    checkSelection(selCom)
    tmpGroup = pm.group(selCom[:-1])
    pm.parent(tmpGroup, selCom[-1])
    tmpGroup.rotate.set([0, 0, 0])
    tmpGroup.translate.set([0, 0, 0])
    pm.parent(tmpGroup, world = True)
    pm.ungroup(tmpGroup)
    # Convert controls to control vertices
    selCom2 = selCom[:-1]

    for i in range(len(selCom2)):
        selCom2[i] += '.cv[*]'

    pm.select(selCom2)
    pm.rotate([0, 0, 90])
    pm.select(cl = True)
    pm.select(selCom[:-1])


# -----------------------------------------------------------------------------------
# Change controller name to JOINT_NAME_ctrl
# -----------------------------------------------------------------------------------

def renameCtrlToJnt():
    checkSelection()

# -----------------------------------------------------------------------------------
# Freeze Selected Components
# -----------------------------------------------------------------------------------

def freezeAll():
    selCom = pm.ls(sl = True, fl = True)
    pm.makeIdentity(selCom, apply = True, t = 1, r = 1, s = 1)

# -----------------------------------------------------------------------------------
# Create Shelf Button
# -----------------------------------------------------------------------------------
def createShelfBtn():
    # Get top shelf as parent
    pm.mel.eval('global string $gShelfTopLevel')
    topShelf = pm.mel.eval('$temp = $gShelfTopLevel')
    currentShelf = pm.tabLayout(topShelf, query=True, selectTab=True)
    pm.setParent(topShelf + '|' + currentShelf)

    # Create the button
    pm.shelfButton(
    annotation = 'myRigTool',
    command =
    'python(\"import sys\");\n'
    '\n'
    'catchQuiet ( `python(\"del sys.modules[\'myRigTool\']\")`);\n'
    'catchQuiet ( `python(\"del sys.modules[\'myRigTool.UI\']\")`);\n'
    'catchQuiet ( `python(\"del sys.modules[\'myRigTool.core\']\")`);\n'
    '\n'
    'python(\"import myRigTool\");',
    label='myRigTool',
    image1='commandButton.png',
    sourceType='mel'
    )
# -----------------------------------------------------------------------------------
