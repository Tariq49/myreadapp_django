from django import template

# Singleton
# meaning, each time you add a filter, you need to restart your server
register = template.Library()

@register.filter
def semi_colon_separator(value):
    return value.replace(', ', '; ')

@register.filter
def join_with_comma(queryset):
    return ', '.join(str(item) for item in queryset)