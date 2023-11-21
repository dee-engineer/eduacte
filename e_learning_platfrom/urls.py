
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from courses.views import CourseListView

urlpatterns = [
    # --- auth routes(done)
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # ---admin panel(done)
    path('admin/', admin.site.urls),
    # ---Course Views (Done)
    path('course/', include('courses.urls')),
    path('', CourseListView.as_view(), name='course_list'),
    # ---Student Views (Done)
    path('students/', include('students.urls')),
    # ---the chat rooms for the courses
    path('chat/', include('chat.urls', namespace='chat/')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)