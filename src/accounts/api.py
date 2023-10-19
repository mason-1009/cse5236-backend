from ninja import Router
import logging

router = Router()
logger = logging.getLogger(__file__)


@router.get('/')
def hello_world(request):
    '''
    Hi :)
    '''
    response = {
        'message': 'Hello, world! :)',
    }

    return response
