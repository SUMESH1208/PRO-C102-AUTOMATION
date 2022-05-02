from os import access
from tracemalloc import start
import cv2
import dropbox
import time
import random

starttime = time.time()

def takesnapshot():
    number = random.randint(0,100)
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videocaptureobject.read()
        imagename = "img" + str(number) + ".png"
        cv2.imwrite(imagename,frame)
        starttime = time.time()
        result = False
    print("Snapshot taken")
    videocaptureobject.release()       
    return imagename 
def upload_file(imagename):
    access_token = "sl.BFsIPKtSAqNNf8Q8sGws_z2nFh_mjdmWzbVdotqoSqas0rc8Zdhkm0PuFxE6thNyGwW_OVpHJQk4NI9h7S8ezthH3sY0hBcYkO71okhRCazv6iNuFEqjjeNP-19S_RD-VRP0Q2-e190e"
    file = imagename
    file_from = file
    file_to = "/test_folder/" + (imagename)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("files_upload")    

def main():
    while(True):
        if((time.time()-starttime)>=5):
            name = takesnapshot()
            upload_file(name)

main()
