import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # this is used to get the current date and time and gives the format as m_d_Y_H_M_S
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # used to get the logs path and concatenate it with the current working dir and the log file name
os.makedirs(logs_path,exist_ok=True) # this is used to create the logs path if it doesn't exist

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) # used to get the log file path and concatenate it with the logs path and the log file name

logging.basicConfig(    # this is used to configure the logging 
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # this is used to format the logging message
    level=logging.INFO, # this is used to set the logging level
)

