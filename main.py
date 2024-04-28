import gdown
import os 
import glob
from datetime import datetime

today = datetime.today()

formatted_date = today.strftime("%Y-%m-%d")

url = 'https://drive.google.com/drive/folders/1sa1GJzLzwSDQyQPqzaIjzOD90kHnZe2E'
gdown.download_folder(url, quiet=True, use_cookies=False)

files = glob.glob('files/*txt')

for file in files:
  new_file_name = file.replace('.txt', f'-{formatted_date}.txt')
  os.rename(file, new_file_name)
