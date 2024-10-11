from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from recipe.models import User,Recipes,Category
from recipe.serial import RecipeSerializers
from rest_framework.exceptions import AuthenticationFailed
import datetime
from rest_framework import status
from rest_framework.decorators import APIView
import jwt



# Create your views here.
def index(request):
    return HttpResponse("Welcome")


def home(request):
    return render(request,"home.html")


class CreateUserView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.create(email=email,password=password)
            user.set_password(password)
            user.save()
        except Exception as e:
            return HttpResponse(e)
        return HttpResponse('User Created')


class AccountDelete(APIView):
    def post(self,request):
        payload = authenticate(request)
        user = User.objects.filter(id=payload['id'])
        user.delete()
        return HttpResponse('User Deleted')


class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        user.is_active = True
        user.save()
        
        if not user:
            raise AuthenticationFailed("No user found by this email")
        if email is None:
            raise AuthenticationFailed("Email id not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Password incorrect")        

        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }

        token = jwt.encode(payload,'secret',algorithm='HS256')

        response = Response()
        # response.set_cookie(key='jwt',value=token,httponly=True)
        # print(token)
        response.data={
            'jwt':str(token),
            'is_active':user.is_active
        }
        return response
    
class LogoutView(APIView):
    def post(self,request):
        payload = authenticate(request)
        user = User.objects.filter(id=payload['id'])
        if not user[0].is_active:
            raise AuthenticationFailed('Already a Looged OUT')
        User.objects.filter(id=payload['id']).update(is_active=False)
        user = User.objects.filter(id=payload['id'])
        # user.is_active = False
        # user.save()
        response = Response()
        response.data={
            'email':user[0].email,
            'is_active':user[0].is_active
        }
        return response


class CreateRecipeView(APIView):
    def post(self, request):
        # Get data from request
        payload = authenticate(request)
        
        category_id = request.data.get('category')
        title = request.data.get('title')
        description = request.data.get('description')
        ingredients = request.data.get('ingredients')
        preparation_steps = request.data.get('preparation_steps')
        owner = payload['id']
        

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category does not exist'}, status=400)

        recipe = Recipes(
            category=category,
            title=title,
            description=description,
            ingredients=ingredients,
            preparation_steps=preparation_steps,
            owner=owner
        )
        recipe.save()
        return Response({'Message': 'Saved successfully!'}, status=201)
    
class RecipeListView(APIView):
    def get(self,request):
        recipe_set = Recipes.objects.all()
        serialized_recipe = RecipeSerializers(recipe_set,many=True)
        return Response(serialized_recipe.data)

class UpdateRecipe(APIView):
    def put(self, request, pk):
        # Fetch the recipe by its primary key (ID)
        try:
            recipe = Recipes.objects.get(pk=pk)
        except Recipes.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)
        
        payload = authenticate(request)
        if payload['id'] != recipe.owner:
            return Response({'error': 'You are not the owner of this Recipe'})
        # Deserialize the incoming data and validate it
        serializer = RecipeSerializers(recipe, data=request.GET, partial=True)  # partial=True allows updating only specific fields

        if serializer.is_valid():
            # Save the updated recipe
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteView(APIView):
    def delete(self,request,pk):
        try:
            recipe = Recipes.objects.get(pk=pk)
        except Recipes.DoesNotExist:
            return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)
        
        payload = authenticate(request)
        if payload['id'] != recipe.owner:
            return Response({'error': 'You are not the owner of this Recipe'})
        recipe.delete()
        return Response({'Message': 'Recipe Deleted Successfully'}, status=status.HTTP_200_OK)
        
        
class AddCategory(APIView):
    def post(self,request):
        category = request.data.get('name')
        category = Category(name=category)
        category.save()
        return Response({'Message': 'Recipe category Added Successfully'}, status=status.HTTP_200_OK)

class FilterView(APIView):
    def post(self,request):
        field = request.data.get('field')
        value = request.data.get('value')
        # payload = authenticate(request)
        recipe = Recipes.objects.all()
        if field == 'category':
            recipe = Recipes.objects.filter(category=value)
        elif field == 'ingredients':
            recipe = Recipes.objects.filter(ingredients=value)
        elif field == 'cooking time':
            recipe = Recipes.objects.filter(cooking_time=value)
        
        serialized_recipe = RecipeSerializers(recipe,many=True)
        return Response(serialized_recipe.data) 


def authenticate(request):
    auth_header = request.headers.get('Authorization')
    try:
        payload = jwt.decode(auth_header[7:],'secret',algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('unauthenticated!')
    
    return payload
