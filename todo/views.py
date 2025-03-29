from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models, serializers

class TodoListApiView(ListCreateAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer

    def post(self, request, *args, **kwargs):
        validator = serializers.TaskValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        title = validator.validated_data.get('title')
        description = validator.validated_data.get('description')
        completed = validator.validated_data.get('completed')
        task = models.Task.objects.create(title=title,
                                          description=description,
                                          completed=completed)
        return Response(data=serializers.TaskSerializer(task).data, status=HTTP_200_OK)




class TodoDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        task_id = models.Task.objects.get(id=kwargs['id'])
        validator = serializers.TaskValidateSerializer(data=request.data)
        validator.is_valid(raise_exception=True)
        task_id.title = validator.validated_data.get('title')
        task_id.description = validator.validated_data.get('description')
        task_id.completed = validator.validated_data.get('completed')
        task_id.save()
        return Response(data=serializers.TaskSerializer(task_id).data, status=HTTP_200_OK)






