from fastapi import APIRouter
from config.log.log import logger


router = APIRouter(prefix='/api/v1/login', tags=[''])

@router.get('/')
def login():
    
    logger.warn('Intento de acceso fallido')
    return {"detail": "login successfull"}