import random
import string
from .models import AccessCode


def generate_access_code(class_level):
    length = 6
    characters = string.ascii_letters + string.digits
    access_code = f'{class_level}_{"".join(random.choice(characters) for _ in range(length - len(str(class_level))))}'
    return access_code


def check_access_code(code):
    try:
        access_code = AccessCode.objects.get(code=code)
        if not access_code.used:
            access_code.used = True
            access_code.save()
            return True
    except AccessCode.DoesNotExist:
        pass

    return False
