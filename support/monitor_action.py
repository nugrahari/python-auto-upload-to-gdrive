import tempfile
import os, sys, datetime, time, json, subprocess
from watchdog.events import PatternMatchingEventHandler
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
drive = GoogleDrive(gauth)  


import logging
logging.basicConfig(filename="support/monitor.log", level=logging.INFO)


class Monitor(PatternMatchingEventHandler):
    def on_created(self, event):
        try:
            print('src:', event.src_path) # print(sys.argv[2])1gT-md6b9VZBF6YcP41M_5lqpl31NbQx9

            gfile = drive.CreateFile({'parents': [{'id': '1gT-md6b9VZBF6YcP41M_5lqpl31NbQx9'}]})

            # Read file and set it as the content of this instance.
            gfile.SetContentFile(event.src_path)
            gfile.Upload() # Upload the file.
            
            logging.info(f'src: {event.src_path} | SUCCES')
        except Exception as e:
            
            logging.error(F'src: {event.src_path} | {e}')
            print(e)

    