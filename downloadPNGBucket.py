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
logging.basicConfig(format='%(levelname)s:%(lineno)s:%(message)s',level=logging.INFO)

def downloadImage(s3Key):
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

def startProcess():
    blrst = bucket.list()
    totalcount = 0
    for k in blrst:
        logging.info('key name: ' + k.name)
        if k.name.endswith('.png'):
            totalcount = totalcount + 1
    logging.info('number of keys: ' + str(totalcount))
    size = 0
    count = 0
    for k in blrst:
        while count < startFrom:
            pass
        logging.info('key name: ' + k.name)
        if k.name.endswith('.png'):
############################################################################        
            startTime = time.clock()
            count = count + 1
            size = size + k.size
            logging.info('processing s3key: %s', k.name)
            downloadImage(k.name)
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
