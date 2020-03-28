import os
cmd = 'pyuic5 ' + os.path.join("ui", "MetabaseExportMain.ui") + ' -o ' + os.path.join("ui", "MetabaseExportMain.py")
os.system(cmd)
