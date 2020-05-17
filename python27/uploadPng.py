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
problemKeys = []

def uploadImage(s3Key, inputFileName):
    if not testRun:
        k = bucket.get_key(s3Key)
        oldacl = k.get_acl()
        k.set_contents_from_filename(inputFileName)
        k.set_acl(oldacl)
    logging.info('Upload FileName: ' + s3Key)
    return

# List keys
#  uploadImage
def startProcess():
    blrst = []
    for root, dirs, files in os.walk(compDir):
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
            try:
                # Read key from key file
                s3Key = open(k + '.key', 'r').readline()
                print 's3key from file ' + s3Key
                #uploadImage(s3Key, k)
            except IOError:
                problemKeys.append(k)
                print 'png file does not contain key file ' + k
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
    for problemKey in problemKeys:
        print 'problemkey: ' + problemKey
############################################################################        
    
if __name__ == "__main__":
    main()
