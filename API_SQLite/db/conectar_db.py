from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

""" Conexxão e ORM """
URL = "sqlite:///<local_do_banco_sqlite>"

engine = create_engine(URL)
sessao = sessionmaker(bind=engine)
base = declarative_base()

def conectar_db_projeto():
    db = sessao()
    try:
        yield db
    finally:
        db.close()

