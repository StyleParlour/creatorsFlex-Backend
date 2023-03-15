from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializers import *
# Create your views here.


@api_view(('GET',))
def home(req):
    return Response('All Works', status=status.HTTP_200_OK)

@api_view(('POST',))
def signupView(req):
    if req.method == 'POST':
        name = req.data['name']
        email = req.data['email']
        password = req.data['pass']
        user = User.objects.create_user(email=email, password=password,name=name)
        return Response('User created Successfully', status=status.HTTP_201_CREATED)
    return Response('It Works Welcome to Signup endpoint', status=status.HTTP_200_OK)

def uploadContent(req):
    if req.method == 'POST':
        email = req.data['email']
        content = req.data['content']
        caption = req.data['caption']
        hashtags = req.data['hashtags']
        uploadAt = req.data['uploadAt']
        user = User.objects.get(email=email)
        account = SocialLogin.objects.get(belongsTo=user)
        content = Content.objects.create(user=user,content=content,caption=caption,hashTags=hashtags, uploadAt=uploadAt,uploadToAccount=account)
        content.save()
        return Response('Content Uploaded Successfully', status=status.HTTP_201_CREATED)
    return Response('It Works Welcome to Content Upload endpoint', status=status.HTTP_200_OK)


def addSocialLogin(req):
    if req.method == 'POST':
        data = req.data
        serializer = SocialSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Added Social Auth successfully", status=status.HTTP_201_CREATED)
        return Response({"data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response("It works welcome to social upload page", status=status.HTTP_200_OK)



@api_view(('GET','POST'))
def contact(req):
    if req.method == "POST":
        data = req.data
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Thanks for contacting us! We'll get back to you soon.", status=status.HTTP_201_CREATED)
        return Response({"Invalid Data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    return Response("Welcome to contact endpoint", status=status.HTTP_201_CREATED)