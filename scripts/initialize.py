import config
import boto
import boto.s3
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
