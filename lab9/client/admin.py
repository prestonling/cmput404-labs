# Register your models here.
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ('user',)
# http POST http://127.0.0.1:8000/api/snippets/ "Authorization:Token 07be9c96d4e9e79d287152e0c9a5687ac5c39a27" code="print('Token works')"
