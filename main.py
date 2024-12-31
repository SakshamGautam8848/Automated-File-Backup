import os
import shutil
import datetime
import schedule
import time

source_dir = "C:/Users/Saksham/Pictures/PyFile" # enter the folder path which you want to backup
destination_dir = "C:/Users/Saksham/Desktop/BackUp" # enter the folder path where you want to backup

def copy_folder_to_destination(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    
    try:
        shutil.copytree(source, dest_dir) #copytree copies recursively as in it copies everything inside the folder
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"FOlder already exists in: {dest}")

schedule.every().day.at("17:01").do(lambda: copy_folder_to_destination(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
