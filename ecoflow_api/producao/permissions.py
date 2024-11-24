from rest_framework.permissions import BasePermission

class IsProdutor(BasePermission):
    """
    Permissão personalizada para garantir que apenas produtores relacionados ao lote
    possam adicionar ou modificar informações de produção.
    """
    def has_object_permission(self, request, view, obj):
        # Verifica se o usuário é o produtor relacionado ao objeto
        return obj.produtor == request.user
