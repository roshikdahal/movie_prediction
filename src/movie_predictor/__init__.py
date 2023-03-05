import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir = "logs"
#creating log directory
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    format=logging_str,
    #write the log in file
    handlers=[
        logging.FileHandler(log_filepath),
        
    ])

logger = logging.getLogger("movie_predictor")