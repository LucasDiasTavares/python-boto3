# Python Boto3 Exemplo Simplificado

Este projeto contém um script Python para interagir com o Amazon S3, usando as bibliotecas boto3 e python-decouple. Ele permite a criação de uma sessão AWS, o upload de um arquivo para um bucket S3 e a listagem de todos os objetos presentes no bucket.


### Requisitos
- Python 3.11.9

### Instalação

Instale as dependências necessárias com os seguintes comandos:
- `pip install boto3`
- `pip install python-decouple`

### Configuração
Crie um arquivo `.env` na raiz do seu projeto com as seguintes variáveis de ambiente:
```
AWS_ACCESS_KEY_ID=your_aws_access_key_id
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
AWS_S3_REGION_NAME=your_aws_s3_region_name
AWS_STORAGE_BUCKET_NAME=your_aws_storage_bucket_name
```

Substitua `your_aws_access_key_id`, `your_aws_secret_access_key`, `your_aws_s3_region_name` e `your_aws_storage_bucket_name` pelos valores apropriados da sua conta AWS.

### Uso

- 1. Defina o caminho do arquivo (file_path) e o nome do objeto (object_name) que deseja fazer upload para o bucket S3.
- 2. Execute o script para fazer o upload e listar os objetos no bucket: `python boto_test.py`

### Observações

- Certifique-se de que o arquivo `.env` está corretamente configurado com suas credenciais AWS antes de executar o script.
- Verifique se você tem permissões adequadas no bucket S3 para realizar uploads e listagens de objetos.
