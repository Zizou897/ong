
from .models import (
    Cas
)


def get_some_cas(data=dict()):
    return Cas.objects.filter(**data).order_by('created_at')[:5]

def get_all_cas(data=dict()):
    return Cas.objects.filter(**data).order_by('created_at').all()
