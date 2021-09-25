import sys
from cx_Freeze import setup, Executable



build_exe_options = {'packages': ['os'], 'includes': ['tkinter','pybank_classes']}


base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Pybank",
    version="0.1",
    description="Banco",
    options={"build_exe": build_exe_options},
    executables=[Executable("pybank_interface.py", base=base)]
)