from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Profile, SwapRequest
from .serializers import RegisterSerializer, ProfileSerializer, SwapRequestSerializer

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# ----------------------
# AUTH VIEWS
# ----------------------

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        tokens = get_tokens_for_user(user)
        return Response(tokens, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        tokens = get_tokens_for_user(user)
        return Response(tokens)
    return Response({'error': 'Invalid credentials'}, status=401)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_user_me(request):
    return Response({"username": request.user.username})

# ----------------------
# PROFILE VIEWS
# ----------------------

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def my_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return Response({"detail": "Profile not found."}, status=404)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

@api_view(['GET'])
@permission_classes([AllowAny])
def public_profiles(request):
    profiles = Profile.objects.filter(public=True)

    skill = request.GET.get('skill')
    availability = request.GET.get('availability')
    location = request.GET.get('location')

    if skill:
        profiles = profiles.filter(skills__icontains=skill)
    if availability:
        profiles = profiles.filter(availability=availability)
    if location:
        profiles = profiles.filter(location__icontains=location)

    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)

# ----------------------
# SWAP VIEWS
# ----------------------

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
    all_requests = sent.union(received).order_by('-updated_at')
    serializer = SwapRequestSerializer(all_requests, many=True)
    return Response(serializer.data)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_swap_status(request, pk):
    try:
        swap = SwapRequest.objects.get(id=pk)
    except SwapRequest.DoesNotExist:
        return Response({"detail": "Not found"}, status=404)

    if swap.receiver != request.user and swap.requester != request.user:
        return Response({"detail": "Not authorized"}, status=403)

    new_status = request.data.get("status")
    allowed_statuses = {
        swap.receiver: ["accepted", "rejected"],
        swap.requester: ["cancelled"]
    }

    if new_status not in allowed_statuses.get(request.user, []):
        return Response({"detail": "Invalid status change"}, status=400)

    swap.status = new_status
    swap.save()
    return Response(SwapRequestSerializer(swap).data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_swap_request(request, pk):
    try:
        swap = SwapRequest.objects.get(id=pk, requester=request.user, status='pending')
    except SwapRequest.DoesNotExist:
        return Response({"detail": "Not found or not allowed"}, status=404)

    swap.delete()
    return Response({"detail": "Deleted"}, status=204)
