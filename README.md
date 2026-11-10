# TP03 - Docker Compose

**Disciplina:** Arquitetura de Serviços em Nuvem (UNISANTA)
**Aluno:** Victor Hugo Soares Matos Brandão

Ambiente com **dois containers** orquestrados por Docker Compose:

| Serviço | Imagem | Porta (host:container) | Descrição |
|---------|--------|------------------------|-----------|
| `site`  | `meu-site-nginx:1.0` (customizada, base `nginx:alpine`) | 8080:80 | Site estático (`index.html`) |
| `api`   | `minha-api-python:1.0` (customizada, base `python:3.11-slim`) | 8081:8000 | API HTTP simples em Python que retorna JSON |

## Estrutura

```
.
├── docker-compose.yml
├── site/
│   ├── Dockerfile
│   └── index.html
└── api/
    ├── Dockerfile
    └── app.py
```

## Como executar

```bash
# 1. Buildar a imagem customizada do site
docker build -t meu-site-nginx:1.0 ./site

# 2. Subir tudo com Compose (builda a API automaticamente)
docker compose up -d --build

# 3. Testar no navegador
#    http://localhost:8080  -> site (Nginx)
#    http://localhost:8081  -> API (JSON)

# 4. Comandos extras
docker compose ps
docker compose logs -f
docker exec -it tp03_site sh
docker exec -it tp03_api bash

# 5. Encerrar
docker compose down
```
