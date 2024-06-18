# pip install boto3
# pip install python-decouple


from decouple import config
import boto3

# Cria uma sessão com a AWS
session = boto3.Session(
    aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"),
    region_name=config("AWS_S3_REGION_NAME")
)

bucket_name = config("AWS_STORAGE_BUCKET_NAME")

# Cria uma sessão usando S3
s3 = session.resource('s3')

# Acessa o bucket
bucket = s3.Bucket(bucket_name)

# Caminho do arquivo
file_path = ''

# Nome do arquivo
object_name = ''

# Faz upload do arquivo para o bucket
s3.Bucket(bucket_name).upload_file(file_path, object_name)

# Lista todos os objetos no bucket
print(f'Objetos no bucket:')
for obj in bucket.objects.all():
    print(obj.key)

