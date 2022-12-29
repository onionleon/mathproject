from django.urls import path
from . import views

urlpatterns = [

    path("home/", views.home, name="home"),
    path("calculus-calculator/", views.calc_calculator, name="calc_calculator"),
    path("algebra-calculator/", views.alg_calculator, name="alg_calculator"),
    path("about-us/", views.about_us, name="about_us"),
    path("prime-factorization/", views.prime_fac, name="prime_fac"),
    path("greatest-common-divisor/", views.gcd, name="gcd"),
    path("ldet/", views.ldet, name="ldet"),

] 