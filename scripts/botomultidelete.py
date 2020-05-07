import boto
import boto.s3

awsAccessKey = 'awsAccessKey'
awsAccessSecret = 'nvYc/awsAccessSecret'
bucketName = 'ftw-dev-bucketName'
conn = boto.connect_s3(awsAccessKey, awsAccessSecret)
bucket = conn.get_bucket(bucketName)

blrst = bucket.list('bucketName/category')

result = bucket.delete_keys(blrst)
print '========================================================================================================'
print result