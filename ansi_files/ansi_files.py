import pathlib

this_path = pathlib.Path(__file__)
datafiles_path = this_path.parent / "datafiles"
# datafiles_path = pathlib.Path("datafiles")
ansi_map = {}
for directory in datafiles_path.iterdir():
    resource = directory.parts[-1]
    ansi_map[resource] = []
    for file in directory.glob("*"):
        ansi_map[resource].append(file)
print(ansi_map)