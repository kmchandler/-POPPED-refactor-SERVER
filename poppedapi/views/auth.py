from rest_framework.decorators import api_view
from rest_framework.response import Response
from poppedapi.models import User


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has associated User

    Method arguments:
      request -- The full HTTP request object
    '''

    uid = request.data['uid']

    try:
        user = User.objects.get(uid=uid)

        data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            "image_url": user.image_url,
            'uid': user.uid
        }
        return Response(data)
    except:
        data = { 'valid': False }
        return Response(data)

@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    user = User.objects.create(
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        username=request.data['username'],
        image_url=request.data['image_url'],
        uid=request.data['uid']
    )

    data = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            "image_url": user.image_url,
            'uid': user.uid
    }
    return Response(data)
