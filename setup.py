import cx_Freeze


executables = [cx_Freeze.Executable("main.py")]


cx_Freeze.setup(
        name="sistemasolar19",
        options = {"build_exe": {"packages":["pygame"],
                                 "include_files":["img"]}},
        description="ninguna",
        executables = executables
        
        )
