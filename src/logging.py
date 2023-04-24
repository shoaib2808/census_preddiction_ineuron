import logging
import sys
import os

Path = os.path.join("Logs","log.txt")
os.makedirs('Logs',exist_ok=True)
with open(Path,'w') as file:
    pass

logging.basicConfig(level=logging.INFO,
format='%(asctime)s  %(message)s  [%(filename)s:%(lineno)d] ',
      filename=Path,
      filemode='w')