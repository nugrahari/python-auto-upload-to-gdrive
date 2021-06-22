import time, os, sys
from support.monitor_action import Monitor
from watchdog.observers import Observer
from watchdog.observers.polling import PollingObserver


if len(sys.argv)<3 or len(sys.argv)>3:
    

    print("\n\n\tEngine Auto Backup to Gdrive")

    if sys.platform == 'linux':
        print("\n\trun with command : ./auto_upload <path> <id_drive> \n\n")
        
    sys.exit() 

else:
    print("+--------------------------------------------------------+")
    print(f"\tPath for auto upload\t: {sys.argv[1]}")
    print(f"\tID Folder Drive\t\t: {sys.argv[2]}")
    print("+--------------------------------------------------------+")

paths = [sys.argv[1]]

    
if __name__ == "__main__":
    try:
        patterns = "*"
        ignore_patterns = ""
        ignore_directories = False
        case_sensitive = True
        kecilin_monitor = Monitor(patterns, ignore_patterns, ignore_directories, case_sensitive)

        go_recursively = True
        kecilin = PollingObserver()
        # kecilin.schedule(kecilin_monitor, config.get('SOURCE', 'path'), recursive=go_recursively)

        # threads = []
        for i in paths:
            targetPath = str(i)
            kecilin.schedule(kecilin_monitor, targetPath, recursive=go_recursively)
            # threads.append(kecilin)
        kecilin.start()
        # print(threads)
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt as e:
            kecilin.stop()
            kecilin.join()
            
    except Exception as e:
        print(e)
        


