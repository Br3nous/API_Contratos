from sqlalchemy import String, Integer
from sqlalchemy.schema import Column
from db.conectar_db import base

class Contratos(base):
    __tablename__ = "TbContratos"
    
    id = Column(String, primary_key=True, autoincrement=True)
    id_acordo = Column(Integer)
    id_contrato = Column(Integer) 
    id_boleto = Column(Integer) 
    nome = Column(String) 
    email = Column(String) 
    idade = Column(Integer)
    valor_emprestimo = Column(String)
    total_parcelas = Column(Integer)
    parcela_atual = Column(Integer) 
    valor_parcela = Column(String)
    valor_total = Column(String)
    dias_atraso = Column(Integer)

    def situacao_contrato(self):
        if Contratos.parcela_atual == Contratos.total_parcelas:
            return "Contrato Quitado."
        else: 
            return "Contrato em Andamento." 