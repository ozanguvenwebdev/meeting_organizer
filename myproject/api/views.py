from django.http import response, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Meeting
from .serializers import MeetingSerializer
from api import serializers
# Create your views here.



@api_view(['GET'])
def getMeetings(request):
    meetings = Meeting.objects.all().order_by('date')
    serializer = MeetingSerializer(meetings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createMeeting(request):
    data = request.data
    serializer = MeetingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateMeeting(request, pk):
    data = request.data
    meeting = Meeting.objects.get(id=pk)
    serializer = MeetingSerializer(instance=meeting, data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteMeeting(request, pk):
    meeting = Meeting.objects.get(id=pk)
    deleted_meeting_id = meeting.id
    meeting.delete()
    return JsonResponse({'id':deleted_meeting_id,'status':'ok'})
