from fastapi import HTTPException, Header
import jwt

""" Configurações e Variáveis """
SEGREDO = "YXBpX2dydXBvZXVybzE3X2NvYm1haXM=" 
ALGORITMO = "HS256"

""" Funções """
def verificar_token(authorization: str = Header(...)):
    try:
        tipo, token = authorization.split()
        if tipo.lower() != "bearer":
            raise HTTPException(status_code=403, detail="Token inválido")
        payload = jwt.decode(token, SEGREDO, algorithms=[ALGORITMO])
        return payload  

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Erro ao processar o token: {str(e)}")