# Aluraflix Backend
Projeto do desafio de backend da Alura focada em construir uma API para a Aluraflix, um frontend já existente.

O desafio foi aberto para escolha de linguagem e banco de dados para construção da API. Eu optei por construir em Python utilizando Django Rest Framework (DRF) e o banco de dados Postgres.

## **BANCO DE DADOS**
  O banco de dados utilizado foi o Postgres, para configurar basta editar as configurações no arquivo *`setup/settings.py`* com os seus dados;
  
  ```language
  DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ‘<db_name>’,
        'USER': '<db_username>',
        'PASSWORD': '<password>',
        'HOST': '<db_hostname_or_ip>',
        'PORT': '<db_port>',
    }
  }
  ```

  Instalar também o cliente Postgres *`pip install psycopg2-binary`*

### **ESTRUTURA DO JSON**
---
   ```JSON
   {
      "titulo": "",
      "descricao": "",
      "url": ""
   }
   ```

### **ENDPOINTS**
---
   ```language
   POST /videos
   ```
---
   ```language
   GET /videos 
   ```
---
   ```language
   GET /videos/{id}/
   ```
---
   ```language
   PUT /videos/{id}/
   ```
---
   ```language
   PATCH /videos/{id}/
   ```
---
   ```language
   DELETE /videos/{id}/
   ```
---