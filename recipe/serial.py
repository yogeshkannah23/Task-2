from recipe.models import Recipes
from rest_framework import serializers

class RecipeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ['id','category','title','description',
                 'ingredients','preparation_steps',
                 'cooking_time','owner','serving_size']
