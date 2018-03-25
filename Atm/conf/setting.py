#coding=utf-8
#Author:gm
import os
BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_SETTING={
    'engine':'file',
    'path':'%s\db'%(BASE_PATH)
}