import sys
import os
import boto
import boto.s3
import time
import datetime
import logging
import config
import shutil

origDir = config.ORIGINAL_DIRECTORY
compDir = config.COMPRESS_DIRECTORY
logging.basicConfig(format='%(levelname)s:%(lineno)s:%(message)s',level=logging.INFO)
testRun = config.TRIAL_RUN

def compressImage(fileName):
    originalFileName = fileName
    compressFileName = fileName.replace(origDir, compDir, 1)
    compressDirectory = compressFileName[0:compressFileName.rfind(os.path.sep)] 
    if not os.path.exists(compressDirectory):
        os.makedirs(compressDirectory)
    if os.path.exists(compressFileName):
        os.remove(compressFileName)    
    if not testRun:
        pngstatus = os.system("pngquant --force " + "\"" + originalFileName + "\"" + " --output " + "\"" + compressFileName + "\"") # add extension?
        shutil.copy(originalFileName + ".key", compressFileName + ".key")
    logging.info('Compress FileName: ' + compressFileName) 
    return compressFileName

def startProcess():
    blrst = []
    for root, dirs, files in os.walk(origDir):
        for file in files:
            if file.endswith(".png"):
             logging.debug(os.path.join(root, file))
             blrst.append(os.path.join(root, file))
    count = 0
    for k in blrst:
        #logging.info('key name: ' + k.name)
        if k.endswith('.png'):
############################################################################        
            startTime = time.clock()
            count = count + 1
            compressFileName = compressImage(k)
            stopTime = time.clock()
            logging.info('one image time taken: %d', stopTime - startTime)
############################################################################        
    logging.info('number of keys: ' + str(count))
    return

def main():
############################################################################        
    startTime = time.clock()
    startProcess()
    stopTime = time.clock()
    logging.info('total time taken: %d', stopTime - startTime)
############################################################################        

if __name__ == "__main__":
    main()
    