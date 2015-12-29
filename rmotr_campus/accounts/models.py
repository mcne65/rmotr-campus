from __future__ import division, unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser

from social.apps.django_app.default.models import UserSocialAuth


class User(AbstractUser):

    @property
    def avatar_url(self):
        """Returns user avatar URL if user has signed up using Github provider,
        or None otherwise"""
        try:
            user_social_auth = self.social_auth.get(provider='github')
            return 'https://avatars.githubusercontent.com/u/{}?v=3'.format(
                user_social_auth.extra_data['id'])
        except UserSocialAuth.DoesNotExist:
            return None
