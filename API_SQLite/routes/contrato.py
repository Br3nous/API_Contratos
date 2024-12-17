from fastapi import APIRouter, Depends, HTTPException
from utils.jwt_utils import verificar_token
from models.contratos import Contratos
from sqlalchemy.orm import Session
from db.conectar_db import conectar_db_projeto

rooter = APIRouter()

@rooter.get("/contratos/{id}")
def obter_contrato_por_id(id: int, db: Session = Depends(conectar_db_projeto), token: str = Depends(verificar_token)):
    contrato = db.query(Contratos).filter(Contratos.id_contrato == id).first()
    if not contrato:
        raise HTTPException(status_code=404, detail="Contrato não encontrado")
    return {

        "Usuario": {
            "ID": contrato.id,
            "Nome": contrato.nome,
            "Email": contrato.email,
            "Idade": contrato.idade
        },
        "Contrato": {
            "IdAcordo": contrato.id_acordo,
            "IdContrato": contrato.id_contrato,
            "ValorDoEmprestimo": f"R$ {contrato.valor_emprestimo}",
            "TotalParcelas": contrato.total_parcelas,
            "ValorParcelas": f"R$ {contrato.valor_parcela}"""
        },
        "Boleto": {
            "IdBoleto": contrato.id_boleto,
            "Parcela": contrato.parcela_atual,
            "SituacaoContrato": contrato.situacao_contrato()
        }
    }

