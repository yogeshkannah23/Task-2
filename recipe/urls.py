from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name='index'),
    path("home/",views.home,name="home"),
    
    
    path("login/",views.LoginView.as_view(),name='login'),
    path("register/",views.CreateUserView.as_view(),name='register'),
    path("delete_account/",views.AccountDelete.as_view(),name='delete_account'),
    path("logout/",views.LogoutView.as_view(),name='logout'),
    
    
    path("list/",views.RecipeListView.as_view(),name='list'),
    
    
    path("create/",views.CreateRecipeView.as_view(),name='create'),
    path("update/<int:pk>",views.UpdateRecipe.as_view(),name='update'),
    path("delete/<int:pk>",views.DeleteView.as_view(),name='delete'),
    
    path("add_category/",views.AddCategory.as_view(),name='add_category'),
    
    path("filter/",views.FilterView.as_view(),name='filter')
]