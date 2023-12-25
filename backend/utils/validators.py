from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

email_regex = RegexValidator(
    regex=r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net|org|info)$",
    message=_("Email must be entered in the format: `abc@abc.com|net|org|info`."),
)
name_regex = RegexValidator(
    regex=r"^[A-z\s]+$",
    message=_("invalid name!."),
)
