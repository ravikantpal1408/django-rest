from rest_framework import serializers
from news.models import Article


class ArticleSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validate_data):
        print(validate_data)
        return Article.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.author = validate_data.get('author', instance.author)
        instance.title = validate_data.get('title', instance.title)
        instance.author = validate_data.get('author', instance.author)
        instance.description = validate_data.get(
            'description', instance.description)
        instance.body = validate_data.get('body', instance.body)
        instance.location = validate_data.get('location', instance.location)
        instance.publication_date = validate_data.get(
            'publication_date', instance.publication_date)
        instance.active = validate_data.get('active', instance.active)
        instance.created_at = validate_data.get(
            'created_at', instance.created_at)
        instance.updated_at = validate_data.get(
            'updated_at', instance.updated_at)

        instance.save()

        return instance

    def validate(self, data):
        ''' check that description and title are different '''
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                'Title and Description must be different')
        return data

    def validate_title(self, value):
        if len(value) < 60:
            raise serializers.ValidationError(
                "The title must be atleast 60 character")
        return value

    def validate_empty_values(self, data):
        return super().validate_empty_values(data)

    def validate_author(self, value):
        if value.strip() == '':
            raise serializers.ValidationError('please enter the author name')
        return value

    def validate_description(self, value):
        if value.strip() == '':
            raise serializers.ValidationError(
                'please enter the description name')
        if len(value) < 50:
            raise serializers.ValidationError(
                'minimum 50 characters required')

        return value
