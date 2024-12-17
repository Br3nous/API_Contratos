from fastapi import FastAPI
from routes.auth import rooter as auth_routes
from routes.contrato import rooter as contrato_routes

""" Definindo API """
api = FastAPI()

""" Registrando Rotas """
api.include_router(auth_routes, prefix="/auth") 
api.include_router(contrato_routes, prefix="/api") 
