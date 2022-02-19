from rest_framework import serializers
from .models import Task, Article


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     author = serializers.CharField(max_length=255)
#     email = serializers.EmailField(max_length=100)
#     datetime = serializers.DateTimeField()


#     def create(self,validated_data):
#         return Article.objects.create(validated_data)

#     def update(self,instance,validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.author = validated_data.get('author', instance.author)
#         instance.email = validated_data.get('email', instance.email)
#         instance.datetime = validated_data.get('datetime', instance.datetime)

#         instance.save()
#         return instance


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
