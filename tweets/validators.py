from django.core.exceptions import ValidationError


#validate the content, can also prevent the use of some words if desired
def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("cannot be blank")
    return value