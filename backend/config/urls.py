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
        description="""You can use JSON examples to test API requests.
---------------------------------------------------------------------------------------------------

                                                JSON test example for the DERIVATIVE calculator


INPUT:

{
    "argument_1": "sin(x)", 
    "argument_2": "x", 
    "argument_3": 1
}

OUTPUT: "cos(x)"


-----------------------------------------------------------------------------------------------------------------------------------

                                                JSON test example for the TAYLOR SERIES calculator

INPUT:

{
    "argument_1": "sin(x)", 
    "argument_2": "x", 
    "argument_3": 16,
    "argument_4": 0
}

OUTPUT: "-x**15/1307674368000 + x**13/6227020800 - x**11/39916800 + x**9/362880 - x**7/5040 + x**5/120 - x**3/6 + x"


--------------------------------------------------------------------------------------------------------------------------------------------


                                                JSON test example for the NEWTON METHOD calculator


INPUT:

{
    "argument_1": "x**2", 
    "argument_2": "x", 
    "argument_3": 2
}

OUTPUT: "2.2500"

----------------------------------------------------------------
                                                JSON test example for the SIMPSON METHOD calculator


INPUT: 

{
    "argument_1": "x**2", 
    "argument_2": "x", 
    "argument_3": 0,
    "argument_4": 1
}

OUTPUT: -


-----------------------------------------------------------------------

                                                JSON test example for the TRAPEZOID METHOD calculator


INPUT:

{
    "argument_1": "x**3", 
    "argument_2": "x", 
    "argument_3": 0, 
    "argument_4": 2,
    "argument_5": 4
}



OUTPUT: "4.25000"

---------------------------------------------------------------------------------------------------------
                                               JSON test example for the RECTANGLE METHOD calculator


INPUT:

{
    "argument_1": "x**2", 
    "argument_2": "x", 
    "argument_3": 0, 
    "argument_4": 2,
    "argument_5": 4
}

OUTPUT: "1.75000"

---------------------------------------------------------------------------------------------------

                                                JSON test example for the DEFINITE INTEGRAL calculator


INPUT: 

{
    "argument_1": "sin(x)", 
    "argument_2": "x",
    "argument_3": 0, 
    "argument_4": 3.14159265358979323846
}


OUTPUT: "2.0000"


-----------------------------------------------------------------------------------------------------
                                              JSON test example for the INDEFINITE INTEGRAL calculator



INPUT:

{
    "argument_1": "x**2", 
    "argument_2": "x"
}


OUTPUT: "x**3/3"

--------------------------------------------------------------------------------------------
                                               JSON test example for the LIMIT CALCULATOR calculator


INPUT:

{
    "argument_1": "1/x**2", 
    "argument_2": "x", 
    "argument_3": "-",
    "argument_4": 0
}


OUTPUT: "oo"


---------------------------------------------------------------------------------------------------



        """,
        version="1.0.0"
    ), name='openapi-schema'),
]
