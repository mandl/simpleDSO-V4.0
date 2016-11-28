"""

  Multi platform cxFreze script

"""

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    'build_exe': {
        'includes': 'atexit'
    }
}

setup(  name = "pyDSO",
        version = "0.3",
        description = "Simple application for data fetching from Uni-T UT2xxxC and UT3xxxC digital storage oscilloscopes.",
        options = options,
        executables = [Executable("simpleDSO.py", base=base)])