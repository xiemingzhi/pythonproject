import xml.etree.cElementTree as ET
import config
import sys
import os
import boto
import boto.s3
import time
import datetime
import logging

#logging.basicConfig(filename='readlxmlProcesspng.log',level=logging.DEBUG)
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.INFO)
# S3 test bucket
# Fill in info in config.py
awsAccessKey = config.ACCESS_KEY_ID
awsAccessSecret = config.ACCESS_KEY_SECRET
bucketName = config.BUCKET_NAME
conn = boto.connect_s3(awsAccessKey, awsAccessSecret)
bucket = conn.get_bucket(bucketName)
origDir = config.ORIGINAL_DIRECTORY
compDir = config.COMPRESS_DIRECTORY
# One timestamp for all the files, time when script was executed
ts = str(long(time.time()))

def connectS3():
    conn = boto.connect_s3(awsAccessKey, awsAccessSecret)
    bucket = conn.get_bucket(bucketName)
    logging.info('Using awsAccessKey: '+awsAccessKey)
    
def downloadImage(s3Prefix, xmlImageName):
    outputFileDir = origDir
    outputFileName = outputFileDir + os.path.sep + xmlImageName
    if not os.path.exists(outputFileDir):
        os.makedirs(outputFileDir)
    k = bucket.get_key(s3Prefix + '/' + xmlImageName)
    k.get_contents_to_filename(outputFileName)
    logging.info('Downloaded FileName: ' + outputFileName)
    return outputFileName

def compressImage(outputFileName, xmlImageName):
    compressFileName = compDir + os.path.sep + xmlImageName 
    if not os.path.exists(compDir):
        os.makedirs(compDir)
    if os.path.exists(compressFileName):
        os.remove(compressFileName)    
    os.system("pngquant --force " + "\"" + outputFileName + "\"" + " --output " + "\"" + compressFileName + "\"") # add extension?
    logging.info('Compress FileName: ' + compressFileName) 
    return compressFileName

# Don't delete the key
def renameImage(s3Prefix, xmlImageName):
    logging.info('Original FileName: ' + xmlImageName)
    k = bucket.get_key(s3Prefix + '/' + xmlImageName)
    logging.info('timestamp: ' + str(ts))
    fileNameRename = xmlImageName + "." + ts
    logging.info('Rename FileName: ' + fileNameRename)
    s3KeyNew = s3Prefix + '/' + fileNameRename
    k.copy(bucketName, s3KeyNew, metadata=None, preserve_acl=True)

def uploadImage(s3Prefix, inputFileName, outputFileName):
    k = bucket.get_key(s3Prefix + '/' + inputFileName)
    oldacl = k.get_acl()
    k.set_contents_from_filename(outputFileName)
    k.set_acl(oldacl)
    logging.info('Uploaded FileName: ' + s3Prefix + '/' + inputFileName)
    return

def main():
    if len(sys.argv)==3:
        filename=sys.argv[1]
        s3Prefix=sys.argv[2]
    else:   
        filename='samplefiles' + os.path.sep + 'ANT_Farm_3_6_720_EN_inner.xml'
        s3Prefix = 'TV/Disney Channel/20150622 Disney NP/ANT Farm'
    tree = ET.parse(filename)
    root = tree.getroot()
    files = root.find('files')
    images = files.find('images')
    for image in images.findall('image'):
        name = image.find('fileName')
        logging.info('FileName in xml: ' + name.text)
        outputFileName = downloadImage(s3Prefix, name.text)
        compressFileName = compressImage(outputFileName, name.text)
        renameImage(s3Prefix, name.text)
        uploadImage(s3Prefix, name.text, compressFileName)
    logging.info('=====================================================')

if __name__ == "__main__":
    main()
