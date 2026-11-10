# Imagem base oficial do Python
FROM python:3.11-slim

# Diretorio de trabalho dentro do container
WORKDIR /app

# Copia a aplicacao (usa apenas a biblioteca padrao, sem dependencias)
COPY app.py .

# Variaveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    APP_PORT=8000

# Documenta a porta (nao publica a porta de verdade)
EXPOSE 8000

# Comando executado quando o container iniciar
CMD ["python", "app.py"]
