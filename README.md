<<<<<<< HEAD
=======
<<<<<<< HEAD
# ProjetoPdf-Back
=======
>>>>>>> 4f31318 (add)

# Backend Leitor de pdf python

## Instalação Windows

Este tutorial serve como guia para realizar a subida do backend em abiente de desenvolvimento, siga os passos a baixo para começar :

```bash
  clone o repositorio na sua maquina 
```

Na barra de pesquisa do windows procure por:

```bash
  Ativar ou desativar recursos do Windows > Subsistema do Windows para Linux [x]
```

Ative a opção ( Subsistema do Windows para Linux )

Baixe o Ubuntu WSL na versão mais estável https://ubuntu.com/wsl , abra o terminal realize as configurações iniciais de Username e Password, Agora você possui um ambinte Linux disponivel no seu Windows via terminal.

Ainda com o terminal aberto, rode os seguintes comandos abaixo:

```bash
  sudo apt-get update 
```

```bash
  sudo apt-get install tesseract-ocr 
```

```bash
  sudo apt-get install tesseract-ocr-por 
```

```bash
  sudo apt-get install poppler-utils 
```


```bash
  sudo apt install python3-pip 
```

OK :) já temos as ferramentas nescessárias

Rode o seguinte comando no terminal para abrir o gerenciador de arquivos do windows

```bash
  explorer.exe .
```

Arraste a pasta do seu projeto zipada para dentro do gerenciador de arquivo, descompacte o arquivo, após isso navegue ate a pasta do projeto, e acesse o seguinte diretório: 

```bash
  cd /PastaProjeto/
```

Execute os comandos a baixo para instalar as bibliotecas do projeto e Criação do Banco de dados e tabelas

```bash
  pip install -r requirements.txt
```

```bash
  mkdir api/sqlite/database/
```

```bash
  mkdir api/uploads/
```

```bash
  mkdir api/uploads/image_pdf/
```

```bash
  python3 api/sqlite/tables/users.py
```

```bash
  python3 api/sqlite/tables/nfs.py
```

Abra o arquivo config localizado na pasta api/utils/config.py edite a variavel path alterando para o caminho absoluto ate a pasta backend do projeto

Para obeter o caminho da pasta, rode o comando:

```bash
  pwd
```
em seguinda altere pegando o caminho /home até a pasta /backend
```bash
  path = '/home/seuUser/pastaDoProjeto'
```

Tudo finalizado 🚀 para inciar a aplicação vá até a pasta backend e rode o comando de start a baixo:

```bash
  python3 api/api.py
```
<<<<<<< HEAD
=======
>>>>>>> 924368f (add)
>>>>>>> 4f31318 (add)
<<<<<<< HEAD
# ProjetoPdf-Back
=======

# Backend Leitor de pdf python

## Instalação Windows

Este tutorial serve como guia para realizar a subida do backend em abiente de desenvolvimento, siga os passos a baixo para começar :

```bash
  clone o repositorio na sua maquina 
```

Na barra de pesquisa do windows procure por:

```bash
  Ativar ou desativar recursos do Windows > Subsistema do Windows para Linux [x]
```

Ative a opção ( Subsistema do Windows para Linux )

Baixe o Ubuntu WSL na versão mais estável https://ubuntu.com/wsl , abra o terminal realize as configurações iniciais de Username e Password, Agora você possui um ambinte Linux disponivel no seu Windows via terminal.

Ainda com o terminal aberto, rode os seguintes comandos abaixo:

```bash
  sudo apt-get update 
```

```bash
  sudo apt-get install tesseract-ocr 
```

```bash
  sudo apt-get install tesseract-ocr-por 
```

```bash
  sudo apt-get install poppler-utils 
```


```bash
  sudo apt install python3-pip 
```

OK :) já temos as ferramentas nescessárias

Rode o seguinte comando no terminal para abrir o gerenciador de arquivos do windows

```bash
  explorer.exe .
```

Arraste a pasta do seu projeto zipada para dentro do gerenciador de arquivo, descompacte o arquivo, após isso navegue ate a pasta do projeto, e acesse o seguinte diretório: 

```bash
  cd /PastaProjeto/
```

Execute os comandos a baixo para instalar as bibliotecas do projeto e Criação do Banco de dados e tabelas

```bash
  pip install -r requirements.txt
```

```bash
  mkdir api/sqlite/database/
```

```bash
  mkdir api/uploads/
```

```bash
  mkdir api/uploads/image_pdf/
```

```bash
  python3 api/sqlite/tables/users.py
```

```bash
  python3 api/sqlite/tables/nfs.py
```

Abra o arquivo config localizado na pasta api/utils/config.py edite a variavel path alterando para o caminho absoluto ate a pasta backend do projeto

Para obeter o caminho da pasta, rode o comando:

```bash
  pwd
```
em seguinda altere pegando o caminho /home até a pasta /backend
```bash
  path = '/home/seuUser/pastaDoProjeto'
```

Tudo finalizado 🚀 para inciar a aplicação vá até a pasta backend e rode o comando de start a baixo:

```bash
  python3 api/api.py
```
>>>>>>> 924368f (add)
