from django.contrib.auth.mixins import PermissionRequiredMixin


class ModerationPermissionMixin(PermissionRequiredMixin):
    permission_required = 'message.moderation'
    permission_denied_message = 'Vous devez être modérateur !'
