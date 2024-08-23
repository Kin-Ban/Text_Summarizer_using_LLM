import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 

project_name="TextSummarizer_llm"

list_of_files=[
    ".github/workflows/.gitkeep",#".github" is used during CI/CD deployment,here we write the .yml file which is required for automatic deployment.Whenever you apply commit in github it automatically gets deployed in the cloud.".gitkeep"-to avoid uploading of empty folder.later on this folder will be deleted.
    f"src/{project_name}/__init__.py",#"__init__" whenever installing the local packages the this constructor file is important.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    file_path=Path(file_path)#to convert the path to our os format
    file_dir,file_name=os.path.split(file_path)#to split the path into directory and file name
    
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating directory {file_dir} for file {file_name}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):#"getsize" give 0 when the file has no content within it.
        with open(file_path,'w') as f:
            pass
        logging.info(f"creating empty file {file_path}")
    else:
        logging.info(f"{file_name} is already present at {file_path}")