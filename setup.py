from cx_Freeze import setup, Executable

setup(name="Batch text file reader", executables=[Executable("Batch text file reader script.py")], options={"build_exe": {"excludes": ["tkinter"]}})
