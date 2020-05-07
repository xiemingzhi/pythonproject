import sys
import os
import boto
import boto.s3
import time
import datetime
import logging
import config

awsAccessKey = config.ACCESS_KEY_ID
awsAccessSecret = config.ACCESS_KEY_SECRET
bucketName = config.BUCKET_NAME
conn = boto.connect_s3(awsAccessKey, awsAccessSecret)
bucket = conn.get_bucket(bucketName)
origDir = config.ORIGINAL_DIRECTORY
compDir = config.COMPRESS_DIRECTORY
logging.basicConfig(format='%(levelname)s:%(lineno)s:%(message)s',level=logging.INFO)
testRun = config.TRIAL_RUN
problemKeys = []

def downloadImage(s3Key):
    originalKey = s3Key
    s3Dir = s3Key[0:s3Key.rfind('/')]
    logging.info('s3Key split: ' + s3Dir)
    outputFileDir = origDir + os.path.sep + s3Dir.replace('/',os.path.sep)
    #outputFileDir = origDir
    s3FileName = s3Key[s3Key.rfind('/')+1:len(s3Key)]
    outputFileName = outputFileDir + os.path.sep + s3FileName
    logging.info('outputfilename: ' + outputFileName)
    if not os.path.exists(outputFileDir):
        try:
            os.makedirs(outputFileDir.encode('string_escape'))
        except OSError:
            problemKeys.append(s3Key)
            logging.error('Unable to create directory: %s', outputFileDir)
            return
    if outputFileDir.endswith(' '):
        problemKeys.append(s3Key)
        logging.error('Directory ends with space: %s', outputFileDir)
        return        
    if os.path.isfile(outputFileName):
        logging.error('file exists: %s, skipping', outputFileName)
        return
    if not testRun:
        k = bucket.get_key(s3Key)
        k.get_contents_to_filename(outputFileName)
        logging.info('Download FileName: ' + s3FileName)
        outputKeyFileName = open(outputFileName + '.key', 'w')
        outputKeyFileName.write(originalKey)
        outputKeyFileName.close()
    
    return s3FileName

# List keys
#  downloadImage
def startProcess():
    blrst = bucket.list()
    count = 0
    size = 0
    for k in blrst:
        #logging.info('key name: ' + k.name)
        if k.name.endswith('.png'):
############################################################################        
            startTime = time.clock()
            count = count + 1
            size = size + k.size
            #downloadImage(s3Prefix, xmlImageName)
            originalFileName = downloadImage(k.name)
            stopTime = time.clock()
            logging.info('one image time taken: %d', stopTime - startTime)
############################################################################        
    logging.info('number of keys: ' + str(count))
    logging.info('total size: ' + str(size))
    return

def main():
############################################################################        
    startTime = time.clock()
    startProcess()
    stopTime = time.clock()
    logging.info('total time taken: %d', stopTime - startTime)
    for problemKey in problemKeys:
        print 'problemkey: ' + problemKey
############################################################################        

if __name__ == "__main__":
    main()
