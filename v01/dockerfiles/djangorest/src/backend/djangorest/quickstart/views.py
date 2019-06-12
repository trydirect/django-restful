from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    """
    @api {post} /users Predict positive rate
    @apiVersion 0.1.0
    @apiName List
    @apiGroup Predict
    @apiDescription Returns the predicted positive rate
    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "success": true,
            "result":{
                "email": "admin@example.com",
                "groups": [],
                "url": "http://localhost:8000/users/1/",
                "username": "paul"
                },
                {
                "email": "tom@example.com",
                "groups": [                ],
                "url": "http://127.0.0.1:8000/users/2/",
                "username": "tom"
                }
        }
    @apiErrorExample Error-Response:
        HTTP/1.1 200
        {
            "success": false,
            "errors":{
                "global_error":{
                    "code": 3066431594,
                    "message": "Not found"
                }
            }
        }

    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
