from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Nif cleaner",
    version = "1",
    description = "Tool to fix nif for blender 2.49b compatibility",
    executables = [Executable("launcher.py")],
)