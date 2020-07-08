import boto3
import botocore
import os, sys
import gzip

client = boto3.client('s3')
s3 = boto3.resource('s3')

bucketName = input("Bucket Name: ")
prefix = input("Prefix: ")
cfDistribuition = input("CloudFront Distributions: ")
date = input("Date: ")
localpath = input("Local Path: ")
url = prefix+"/"+cfDistribuition+"."+date

bucket_conn =  s3.Bucket(bucketName)
obj_conn = bucket_conn.objects.filter(Prefix=url)

print ("Execução Iniciada.")
os.mkdir( localpath, 755 );

print ("Iniciando Downaload.")

f = open(bucketName+".log", "wb")
for obj in obj_conn:
		filename = (obj.key.replace(prefix, ''))
		s3.meta.client.download_file(bucketName, obj.key, localpath+filename)

		with gzip.open(localpath+filename, "rb") as fin:
			for line in fin:
				f.write(line)

f.close()
print("Download concluído com sucesso.")