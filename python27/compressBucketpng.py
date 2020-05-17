import config
import sys
import os
import boto
import boto.s3
import time
import datetime
import logging

awsAccessKey = config.ACCESS_KEY_ID
awsAccessSecret = config.ACCESS_KEY_SECRET
bucketName = config.BUCKET_NAME
conn = boto.connect_s3(awsAccessKey, awsAccessSecret)
bucket = conn.get_bucket(bucketName)
origDir = config.ORIGINAL_DIRECTORY
compDir = config.COMPRESS_DIRECTORY
logging.basicConfig(format='%(levelname)s:%(lineno)s:%(message)s',level=logging.INFO)
testRun = config.TRIAL_RUN
startFrom = config.START_FROM

def downloadImage(s3Key):
    #s3Dir = s3Key[0:s3Key.rfind('/')]
    #logging.info('s3Key split: ' + s3Dir)
    #outputFileDir = origDir + os.path.sep + s3Dir
    outputFileDir = origDir
    s3FileName = s3Key[s3Key.rfind('/'):len(s3Key)]
    outputFileName = outputFileDir + os.path.sep + s3FileName
    logging.debug('outputfilename: ' + outputFileName)
    if not os.path.exists(outputFileDir):
        os.makedirs(outputFileDir)
    if os.path.exists(outputFileName):
        logging.error('file exists: %s, will be overwritten', outputFileName)
    if not testRun:
        k = bucket.get_key(s3Key)
        k.get_contents_to_filename(outputFileName)
    logging.info('Download FileName: ' + s3FileName)
    return s3FileName

def compressImage(fileName):
    originalFileName = origDir + os.path.sep + fileName
    compressFileName = compDir + os.path.sep + fileName 
    if not os.path.exists(compDir):
        os.makedirs(compDir)
    if os.path.exists(compressFileName):
        os.remove(compressFileName)    
    if not testRun:
        pngstatus = os.system("pngquant --force " + "\"" + originalFileName + "\"" + " --output " + "\"" + compressFileName + "\"") # add extension?
        logging.info('Compress FileName: ' + compressFileName) 
        return compressFileName, pngstatus
    else:
        return compressFileName,1

def uploadImage(s3Key, inputFileName):
    if not testRun:
        k = bucket.get_key(s3Key)
        oldacl = k.get_acl()
        k.set_contents_from_filename(inputFileName)
        k.set_acl(oldacl)
    logging.info('Upload FileName: ' + s3Key)
    return

# List keys
#  downloadImage
#  compressImage
#  uploadImage
def startProcess():
    blrst = bucket.list()
    totalcount = 0
    for k in blrst:
        #logging.info('key name: ' + k.name)
        if k.name.endswith('.png'):
            totalcount = totalcount + 1
    logging.info('number of keys: ' + str(totalcount))
    size = 0
    count = 0
    for k in blrst:
        count = count + 1
        #logging.info('count: %d', count)
        if count < startFrom:
            continue
        #logging.info('key name: ' + k.name)
        if k.name.endswith('.png'):
############################################################################        
            startTime = time.clock()
            size = size + k.size
            logging.info('processing s3key: %s', k.name)
            originalFileName = downloadImage(k.name)
            compressFileName, pngstatusreturn = compressImage(originalFileName)
            if pngstatusreturn == 0:
                uploadImage(k.name, compressFileName)
            stopTime = time.clock()
            logging.info('one image time taken: %d', stopTime - startTime)
            logging.info('completed: %d, of %d', count, totalcount)
############################################################################        
    logging.info('total size: ' + str(size))
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
