import logging
import os

# Create a custom logger
logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

path = "logs"

if not os.path.exists(path):
    os.makedirs(path)
    print("The log directory created")

# Create handlers
c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('logs/logger.log')
f_handler = logging.handlers.TimedRotatingFileHandler(
    filename=f'logs/general.log', when='D', interval=1, backupCount=4
)

# Create formatters and add it to handlers
c_format = logging.Formatter(
    '%(module)s - %(pathname)s - %(levelname)s - %(message)s')
f_format = logging.Formatter(
    '%(asctime)s - %(module)s - %(pathname)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
