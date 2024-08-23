import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"#it will log the time,the level name used such as "info",the module name is logged like if running main.py then module name "main" is logged,and the message you want to log is logged.
#[2024-08-21 01:19:37,847: INFO: main: Welcome to Text Summarization Project]

log_dir = "logs" # logs folder
log_file_path = os.path.join(log_dir, "running_logs.log") #log file path
os.makedirs(log_dir, exist_ok=True) #if the folder does not exist it will create it

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_file_path),#it will log in a file
        logging.StreamHandler(sys.stdout)#as well as it will show in the terminal
    
    ]
)

logger=logging.getLogger("textSummarizerLogger")