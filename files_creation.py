import os
import logging
from pathlib import Path

logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "WasteDetection"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trails.ipynb"
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)

    # first create folders
    filedir , filename = os.path.split(filepath)
    if filedir != "": # if file directory is not epmty
        os.makedirs(filedir, exist_ok= True) # exist_Ok means if directory exist before do not create it again
        logging.info(f" Creating directory {filedir} for the file {filename}")
    if (not os.path.exists(filename)) or (os.path.getsize(filename)== 0): # or file is empty
        with open(filepath, "w") as f:
            pass 
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f" {filename} is already created")