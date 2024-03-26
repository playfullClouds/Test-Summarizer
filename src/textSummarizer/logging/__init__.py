import logging
import os
import sys
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs", LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    # filename=LOG_FILE_PATH,
    format="[ %(asctime)s - %(levelname)s - %(module)s -%(message)s]",
    level = logging.INFO,
    
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)


logger = logging.getLogger("textSummarizerLogger")

# if __name__ == '__main__':
#     logging.info("Logging has started")