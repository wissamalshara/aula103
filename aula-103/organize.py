import os
import shutil
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/wissa/Downloads"
to_dir = "C:/Users/wissa/Desktop/arquivos e documentos"

dir_tree ={
    "image_files": [".jpg", ".jpeg", ".png", ".gif"],
    "video_files": [".mpg", ".mp2", ".mpeg", ".mpe", ".mp4", ".m4v", ".avi", ".mov"],
    "document_files": [".pdf", ".txt", ".csv", ".xls", ".ppt"],
    "setup_files": [".exe", ".bin", ".cmd", ".msi", ".dmg"]
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        name, extension = os.path.splitext(event.src_path) 
        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Baixado")
                path1 = from_dir + "/" +  file_name
                path2 = to_dir + "/" +  key
                path3 = to_dir + "/" + key +  "/" + file_name
                time.sleep(1)
                if os.path.exists(path2):
                 print("Diretório existe")
                 time.sleep(1)
                 if os.path.exists(path3):
                    print("O arquivo já existe em: " + key + "..." )
                    print("Renomeando arquivo " + file_name + "...")
                    new_file_name = os.path.splitext(file_name)[0]+ str(random.randint(0,999 )) + os.path.splitext(file_name)[1]
                    path4 = to_dir + "/" + key + "/" + new_file_name
                    print("Movendo")
                    shutil.move(path1, path4)
                    time.sleep(1)
                 else:
                  print("movendo")
                  shutil.move(path1, path3)
                  time.sleep(1)

                else:
                   print("Criando diretório")
                   os.makedirs(path2)
                   print("movendo")
                   shutil.move(path1, path3)
                   time.sleep(1)

eventHandler = FileMovementHandler()
observer = Observer()  
observer.schedule(eventHandler, from_dir, recursive = True)
observer.start()
try: 
   while True:
      time.sleep(2)
      print("Executando")
except KeyboardInterrupt:
   print("Interrompido")
   observer.stop()

          
            
     



