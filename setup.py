import sys
from cx_Freeze import setup, Executable

# Replace "your_script.py" with the name of your Python script
script = "GUI_main.py"

# Create the executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Use this for Windows GUI applications

exe = Executable(
    script,
    base=base,
)

# Configure the setup options
options = {
    "build_exe": {
        "include_files": [],  # Add any additional files or data needed by your script
    },
}

# Run the setup
setup(
    name="YourScript",
    version="1.0",
    description="Description of your script",
    options=options,
    executables=[exe],
)
