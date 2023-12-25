from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpRequest
import random
import string


def get_url(request=None):
    request = request or HttpRequest()
    domain = get_current_site(request).domain
    return "{0}{1}".format(domain, request.get_full_path())


def unique_code(n: int):
    """
    ♻Reuseable function that generate random unique code based on input value.
    param: n (int)
        n: number of characters in the code
    return:
        code: unique code based on input value
    """
    allowed_digits = "".join((string.digits))
    unique_code = "".join(random.choice(allowed_digits) for _ in range(n))
    return unique_code
