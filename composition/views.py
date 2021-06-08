from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from composition.models import Memo
from composition.serializers import MemoSerializer


@api_view(['POST'])  # HTTP 메소드 중 POST를 사용
@permission_classes([AllowAny])  # 모든 종류의 데이터를 허용
def create_memo(request):
    serializer = MemoSerializer(data=request.data)

    if not serializer.is_valid(raise_exception=True):
        return Response({"message": "text mustn't be blank"}, status=status.HTTP_409_CONFLICT)

    serializer.save()
    return Response({"message": "success"}, status=status.HTTP_201_CREATED)

    # if Memo.objects.filter(text=serializer.validated_data['text']).first() is None:
    #     serializer.save()
    #     return Response({"message": "success"}, status=status.HTTP_201_CREATED)
    # return Response({"message": "already exist"}, status=status.HTTP_409_CONFLICT)


@api_view(['GET'])
@permission_classes([AllowAny])
def memo_list(request):
    memo = Memo.objects.all()
    serializer = MemoSerializer(memo, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def remove_memo(request):
    memo1 = Memo.objects.filter(id=request.user.id)
    memo1.delete()
    return Response({"message": "success"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
@permission_classes([AllowAny])
def update_memo(request, memo2_pk):
    memo2 = get_object_or_404(Memo, pk=memo2_pk)
    serializer = MemoSerializer(instance=memo2, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
