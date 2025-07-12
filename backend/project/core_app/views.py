from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Profile, SwapRequest
from .serializers import ProfileSerializer, SwapRequestSerializer

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_user_me(request):
    return Response({"username": request.user.username})


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def my_profile(request):
    profile = request.user.profile

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def public_profiles(request):
    profiles = Profile.objects.filter(public=True)

    # Optional filters
    skill = request.GET.get('skill')
    availability = request.GET.get('availability')
    location = request.GET.get('location')

    if availability:
        profiles = profiles.filter(availability=availability)
    if location:
        profiles = profiles.filter(location__icontains=location)

    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_swap_request(request):
    data = request.data.copy()
    data['requester'] = request.user.id
    serializer = SwapRequestSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_my_swaps(request):
    sent = SwapRequest.objects.filter(requester=request.user)
    received = SwapRequest.objects.filter(receiver=request.user)
    serializer = SwapRequestSerializer(sent | received, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_swap_status(request, pk):
    try:
        swap = SwapRequest.objects.get(id=pk, receiver=request.user)
    except SwapRequest.DoesNotExist:
        return Response({"detail": "Not found"}, status=404)

    new_status = request.data.get("status")
    if new_status not in ["accepted", "rejected"]:
        return Response({"detail": "Invalid status"}, status=400)

    swap.status = new_status
    swap.save()
    return Response(SwapRequestSerializer(swap).data)