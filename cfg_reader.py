import os

#following was made by AI
CONFIG_DIR = "configs"

REQUIRED_CONFIGS = {
    "checkrun.cfg",
    "config2.cfg",
    "config3.cfg",
    "config4.cfg",
    "config5.cfg",
}

existing_files = {
    f.name for f in os.scandir(CONFIG_DIR)
    if f.is_file()
}

missing = REQUIRED_CONFIGS - existing_files

if not missing:
    print("Integrity check passed.")
else:
    print("Missing configs:", missing)#ai end