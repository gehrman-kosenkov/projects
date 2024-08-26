
import time
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException, TimeoutException

def rename_downloaded_file(download_directory, from_date_str, to_date_str, station_name):
    try:
        time.sleep(10)
        files = os.listdir(download_directory)
        latest_file = max([os.path.join(download_directory, f) for f in files], key=os.path.getctime)
        
        from_date_str_safe = from_date_str.replace('/', '-')
        to_date_str_safe = to_date_str.replace('/', '-')
        new_filename = f"{station_name}_{to_date_str_safe}.xlsx"
        new_filepath = os.path.join(download_directory, new_filename)

        shutil.move(latest_file, new_filepath)
        print(f"Renamed {latest_file} to {new_filename}")
    except Exception as e:
        print(f"Error reading or renaming the Excel file: {e}")




