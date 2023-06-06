# Use a imagem base do Ubuntu 20.04
FROM ubuntu:20.04

# Instale as dependências necessárias
# Instale as dependências necessárias
RUN apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release \
    unixodbc-dev \
    python3 \
    python3-pip \
    redis-server
    
# Adicione a chave do repositório Microsoft
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Adicione o repositório Microsoft para a versão do Ubuntu atual
RUN curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Atualize os pacotes e instale o driver ODBC do SQL Server
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y \
    msodbcsql18

# Opcional: instale as ferramentas bcp e sqlcmd
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools18

# Adicione o diretório das ferramentas ao PATH
RUN echo 'export PATH="$PATH:/opt/mssql-tools18/bin"' >> ~/.bashrc

# Instale o Python 3 e o pip
RUN apt-get update && apt-get install -y python3 python3-pip && apt-get install -y poppler-utils


ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y tesseract-ocr

RUN apt-get install -y tesseract-ocr-por
# Defina o diretório de trabalho
WORKDIR /app

# Copie o código-fonte para o contêiner
COPY . /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt /app/requirements.txt

# Instale as dependências Python
RUN pip install -r requirements.txt
RUN pip install pyodbc jwt pyjwt celery redis uuid


# Copie o script de inicialização
COPY start.sh /app/start.sh

# Defina permissões de execução para o script de inicialização
RUN chmod +x /app/start.sh

# Defina o comando para executar o script de inicialização
CMD ["sh", "/app/start.sh"]