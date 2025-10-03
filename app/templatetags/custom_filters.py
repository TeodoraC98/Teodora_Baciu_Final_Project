from django import template
from dateutil import parser
register = template.Library()

@register.filter
def divide_hour(value, arg):
    try:
        x= int(value) / int(arg)
        hour,minuts=divmod(x,1)
        hour=int(hour)
        return hour
    except (ValueError, ZeroDivisionError):
        return None
@register.filter
def divide_minuts(value, arg):
    try:
        x= int(value) / int(arg)
        hour,minuts=divmod(x,1)
        hour=int(hour)
        minuts=value - hour*60

        return minuts
    except (ValueError, ZeroDivisionError):
        return None
@register.filter
def date(value):
    try:
       date = parser.parse(value) 
       return date
    except (ValueError, ZeroDivisionError):
        return None
    
@register.filter(name='loop') 
def loop(number):
    return range(number)

@register.filter()
def get_name_by_index(dict,index):
    name=dict[index].get("name")
    return name

@register.filter()
def get_duration_by_index(dict,index):
    duration=dict[index].get("duration")
    return duration

@register.filter()
def ltt(x,y):
    print(x,y)
    if x < y:
        return True
    else:
        return False
@register.filter()
def multiply(x,y):
     return x*y
 
@register.filter()
def list_activities(str):
    list=str.split(",")
    return list