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
# import files
# -----------------------------------------------------------------------------------

import UI as ui

# -----------------------------------------------------------------------------------
# create UI
# -----------------------------------------------------------------------------------
ui.window_creation()
