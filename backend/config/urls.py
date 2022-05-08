"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('APP.urls')),
    path('', lambda request: redirect('docs/', permanent=False)),

    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    path('openapi', get_schema_view(
        title="Mathemagics API",
        description="""Use JSON examples to test API requests. Change inputs with the "string" line in the POST requests.  
---------------------------------------------------------------------------------------------------

                                               DERIVATIVE calculator JSON test example 


INPUT:

argument_1 =  equation \n
argument_2 =  variable \n
argument_3 =  degree

    {
    "argument_1": "sin(x)", 
    "argument_2": "x", 
    "argument_3": 1
    }

OUTPUT: "cos(x)"


-----------------------------------------------------------------------------------------------------------------------------------

                                                TAYLOR SERIES calculator JSON test example

INPUT:

argument_1 =  equation\n
argument_2 =  variable\n 
argument_3 =  number of iterations\n
argument_4 =  centered at

    {
    "argument_1": "sin(x)", 
    "argument_2": "x", 
    "argument_3": 16,
    "argument_4": 0
    }

OUTPUT: "-x**15/1307674368000 + x**13/6227020800 - x**11/39916800 + x**9/362880 - x**7/5040 + x**5/120 - x**3/6 + x"


--------------------------------------------------------------------------------------------------------------------------------------------


                                                NEWTON METHOD calculator JSON test example


INPUT:

argument_1 =  equation \n
argument_2 =  variable \n
argument_3 =  number of iterations

    {
    "argument_1": "x**2", 
    "argument_2": "x", 
    "argument_3": 2
    }

OUTPUT: "2.2500"

----------------------------------------------------------------
                                                SIMPSON METHOD calculator JSON test example


INPUT: 

argument_1 =  equation\n
argument_2 =  variable\n 
argument_3 =  initial point\n
argument_4 =  end point

    {
    "argument_1": "x**2", 
    "argument_2": "x", 
    "argument_3": 0,
    "argument_4": 1
    }

OUTPUT: -


-----------------------------------------------------------------------

                                                TRAPEZOID METHOD calculator JSON test example


INPUT:

argument_1 =  equation\n
argument_2 =  variable\n 
argument_3 =  initial point\n
argument_4 =  end point\n
argument_5 =  number of intervals

    {
    "argument_1": "x**3", 
    "argument_2": "x", 
    "argument_3": 0, 
    "argument_4": 2,
    "argument_5": 4
    }



OUTPUT: "4.25000"

---------------------------------------------------------------------------------------------------------
                                               RECTANGLE METHOD calculator JSON test example


INPUT:

argument_1 =  equation\n
argument_2 =  variable\n 
argument_3 =  initial point\n
argument_4 =  end point\n
argument_5 =  number of intervals

    {
    "argument_1": "x**2", 
    "argument_2": "x", 
    "argument_3": 0, 
    "argument_4": 2,
    "argument_5": 4
    }

OUTPUT: "1.75000"

---------------------------------------------------------------------------------------------------

                                                UNIVERSAL INTEGRAL calculator JSON test example


INPUT: 

argument_1 =  type\n
argument_2 =  equation\n
argument_3 =  variable\n 
argument_4 =  initial point\n
argument_5 =  end point


    {
    "argument_1": "definite", 
    "argument_2": "sin(x)", 
    "argument_3": "x",
    "argument_4": 0, 
    "argument_5": 3.14159265358979323846
    }


OUTPUT: "2.0000"


-----------------------------------------------------------------------------------------------------

                                                DEFINITE INTEGRAL calculator JSON test example


INPUT: 

argument_1 =  equation\n
argument_2 =  variable\n 
argument_3 =  initial point\n
argument_4 =  end point

    {
    "argument_1": "sin(x)", 
    "argument_2": "x",
    "argument_3": 0, 
    "argument_4": 3.14159265358979323846
    }


OUTPUT: "2.0000"


-----------------------------------------------------------------------------------------------------

                                              INDEFINITE INTEGRAL calculator JSON test example



INPUT:

argument_1 =  equation\n
argument_2 =  variable\n 

    {
    "argument_1": "x**2", 
    "argument_2": "x"
    }


OUTPUT: "x**3/3"

--------------------------------------------------------------------------------------------
                                               LIMIT CALCULATOR calculator JSON test example


INPUT:

argument_1 =  equation\n
argument_2 = variable\n
argument_3 = sign, from which side\n
argument_4 = aproaches to

    {
    "argument_1": "1/x**2", 
    "argument_2": "x", 
    "argument_3": "-",
    "argument_4": 0
    }


OUTPUT: "oo"


---------------------------------------------------------------------------------------------------
                                               JSON test example for the  DERIVATIVE TEST GENERATOR calculator


INPUT:

argument_1 = level of the question : from 1 to 3

    {
    "argument_1": "1"
    }

OUTPUT:  "(5*x**2)*(4*x**2)" (each run gives randomly generated question)



        """,
        version="1.0.0"
    ), name='openapi-schema'),
]
