from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from datetime import datetime, timedelta
import jwt

""" Configurações e Variáveis """
SEGREDO = "<Crie a Secret Key>" # Secret Key
ALGORITMO = "HS256"
DURACAO_TOKEN_EM_HORAS = 1

seguranca_basica = HTTPBasic() # Configuração do Basic Auth
rooter = APIRouter() # Criador de Rotas

""" Funções """
def gerar_token(usuario: str) -> str:
    expiracao = datetime.utcnow() + timedelta(hours=DURACAO_TOKEN_EM_HORAS)
    payload = {"sub": usuario, "exp": expiracao}
    token = jwt.encode(payload, SEGREDO, algorithm=ALGORITMO)
    return token

@rooter.post("/login")
def autenticar(credentials: HTTPBasicCredentials = Depends(seguranca_basica)):
    usuario = credentials.username
    senha = credentials.password

    if usuario == "projeto" and senha == "q1w2e3r4":
        token = gerar_token(usuario)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")