import datetime

import xmltodict
import requests
from requests.exceptions import HTTPError

from social.models import Message
from social.providers.base import Provider


class InstagramProvider(Provider):
    def __init__(self, provider):
        super().__init__(provider)

    def fetch_messages(self, feed, **kwargs):
        results = requests.get(
            "https://queryfeed.net/instagram",
            params={
                'q': '#{}'.format(feed.hashtag),
                'token': self.provider.app_secret
            }
        )

        results = xmltodict.parse(results.text)

        if not (results.get('rss') and
                results.get('rss').get('channel') and
                results.get('rss').get('channel').get('item')):
            return

        messages = []
        for item in results['rss']['channel']['item']:

            # Don't store duplicates
            try:
                feed.messages.get(provider_post_id=item['link'])
            except Message.DoesNotExist:
                pass
            else:
                continue

            message = Message()
            # message.author_name = item['']
            # message.author_picture = item['user']['profile_image_url']
            # message.author_username = "@{}".format(item['user']['screen_name'])
            message.author_username = item['guid']
            if 'enclosure' in item:
                media = item['enclosure']
                if 'image' in media['@type']:
                    message.image = media['@url']

            message.text = item['title']

            import pytz
            locale = pytz.utc
            # Thu, 02 Mar 2017 15:13:08 +0000
            message.published_at = locale.localize(
                datetime.datetime.strptime(item['pubDate'], '%a, %d %b %Y %H:%M:%S +0000'))

            message.provider = self.provider
            message.provider_post_id = item['link']
            message.feed = feed
            messages.append(message)
            message.save()
        return messages
