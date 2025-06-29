import logging
from logging.handlers import RotatingFileHandler

# Configure logging to write to both console and a rotating log file
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
log_file = 'test_run.log'
file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
file_handler.setFormatter(log_formatter)
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
console_handler.setLevel(logging.INFO)

def setup_logging():
    # Prevent duplicate handlers if called multiple times
    if not logging.getLogger().handlers:
        logging.basicConfig(level=logging.INFO, handlers=[file_handler, console_handler])
    else:
        # Remove all handlers and re-add
        logging.getLogger().handlers.clear()
        logging.getLogger().addHandler(file_handler)
        logging.getLogger().addHandler(console_handler)
