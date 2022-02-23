from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer


# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html",context={},status=200)


@api_view(['GET'])
def post_detail_view(request,post_id, *args, **kwargs):
    qs=Post.objects.filter(id=post_id)
    if not qs.exists():
        return Response({}, status=404)
    obj=qs.first()
    serializer= PostSerializer(obj)
    return Response(serializer.data)


@api_view(['GET'])
def post_list_view(request, *args, **kwargs):
    qs=Post.objects.all()
    serializer= PostSerializer(qs, many=True)
    return Response(serializer.data)


@permission_classes([IsAuthenticated])
@api_view(['DELETE','POST'])
def post_delete_view(request,post_id, *args, **kwargs):
    qs=Post.objects.filter(id=post_id)
    if not qs.exists():
        return Response({}, status=404)
    qs=qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message":"You cannot delete this post"}, status=401)
    obj=qs.first()
    obj.delete()
    return Response({"message":"Post deleted successfully!!"},status=200)


@api_view(['POST'])
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def post_create_view(request, *args, **kwargs):
    data=request.POST
    serializer=PostSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)




