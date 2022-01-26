from django import template
from customer.models import *
register = template.Library()

@register.inclusion_tag('customer/header.html')





def  category_view(poll):
      choices =Category.objects.all()
      print(choices ,'''''''''''''''''''''''''''''''''''''''''''''''')
      return {'choices': choices}
#----------------------------------