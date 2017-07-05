from cx_Freeze import setup, Executable
setup(
    name ="Bogiasdroid",
    version ="0.1",
    description="Small Backup Program",
    executables=[Executable("BackItUp.py", base = "Win32GUI",icon="ico.ico")]
)