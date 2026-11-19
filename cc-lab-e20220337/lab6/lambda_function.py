import os
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the S3 bucket name and object key from the event
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    # Check the file type
    file_type = os.path.splitext(s3_key)[1][1:].lower()  # get the file extension and convert to lowercase

    # Rename the file to its corresponding folder
    new_s3_key = file_type + '/' + s3_key.split('/')[-1]
    s3.copy_object(
        Bucket=s3_bucket,
        CopySource={'Bucket': s3_bucket, 'Key': s3_key},
        Key=new_s3_key
    )
    s3.delete_object(Bucket=s3_bucket, Key=s3_key)

    # Get the names of each folder with the number of files in them
    folder_names = []
    response = s3.list_objects_v2(Bucket=s3_bucket)
    if 'Contents' in response:
        # Loop through all the objects in the S3 bucket
        for obj in response['Contents']:
            # Skip folders
            if obj['Key'].endswith('/'):
                continue
            # Get the folder name
            folder_name = obj['Key'].split('/')[0]
            if folder_name not in [f[0] for f in folder_names]:
                num_files = sum(
                    1 for _ in s3.list_objects_v2(
                        Bucket=s3_bucket,
                        Prefix=folder_name + '/'
                    )['Contents']
                )
                folder_names.append((folder_name, num_files))

    # Print the count of each type of file
    for folder in folder_names:
        print('We have {} {} file(s).'.format(folder[1], folder[0]))

    return folder_names