from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1'
)


@router.get('/products')
def get_products():
    '''Get all product in the database'''
    pass