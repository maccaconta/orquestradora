# define a imagem base
FROM timon.cloud.prodesp.sp.gov.br/0010053/ppn2-orchest-base:0.0.1

# define diretório de trabalho dentro do contêiner
WORKDIR /usr/src/api-orchest

# variáveis de ambiente
# ----------------------

#impede o Python de copiar arquivos pyc para o contêiner
ENV PYTHONDONTWRITEBYTECODE 1

# garante que a saída Python seja registrada no terminal,
# possibilitando monitorar os registros do Django em tempo real.

ENV PYTHONUNBUFFERED 1

# ENV API_URL=http://ppn2-homol.assistentevirtual.sp.gov.br/orchest/v1/watson/
# ENV API_URL=http://localhost:8000/orchest/v1/watson/

# instala dependências
# ---------------------

# instala e atualiza a versão pip que está no recipiente.
RUN pip install -U pip setuptools


# e instala dependências

COPY ./requirements.txt /usr/src/api-orchest
RUN pip install -r requirements.txt

# copia o código fonte do projeto para o diretório de trabalho no contêiner
COPY . /usr/src/api-orchest


RUN chmod a+w /usr/src/api-orchest/api/static/environment.json

RUN chmod -R a+w /usr/src/api-orchest/api/static/

RUN chmod -R a+w /usr/src/api-orchest/

RUN rm -f /usr/src/api-orchest/.env


# abre a porta 8000 para acesso de outros aplicativos.
EXPOSE 8000


# Define os comandos executáveis no contêiner
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]