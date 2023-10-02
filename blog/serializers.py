from rest_framework import serializers

from blog.models import Post, Categoria

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
    # id = serializers.IntegerField(read_only=True)
    # active = serializers.BooleanField(default=True, required=False)
    # title = serializers.CharField(max_length=100, required=True)
    # author = serializers.CharField(max_length=100, required=False, default='Anonimo', allow_blank=True)
    # content = serializers.CharField(required=True)

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.active = validated_data.get('active', instance.active)
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.save()
    #     return instance

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
