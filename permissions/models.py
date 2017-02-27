import requests
from django.contrib.auth import models as auth_models
from account import models as account_models
from django.db import models

from account.providers import MicrosoftOAuthProvider


class AzureGroup(models.Model):

    group = models.ForeignKey(auth_models.Group)
    azure_id = models.CharField(max_length=100, choices=())

    def check_user(self, user):
        token = account_models.OAuthToken.objects.filter(user=user, service__name='microsoft').last()
        if token is None:
            return False
        result = requests.post(MicrosoftOAuthProvider.graph('/me/checkMemberGroups'), json={
            'groupIds': [self.azure_id]
        }, headers={
            'Authorization': 'Bearer {}'.format(token.auth_token)
        })
        if result.status_code < 300 and self.azure_id in result.json()['value']:
            user.groups.add(self.group)
            return True
        else:
            return False

