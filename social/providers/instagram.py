import datetime
import json
import re

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

            r = requests.get(item['link'])
            user_re = re.compile(r'"owner": ({.*?})')
            m = user_re.search(r.text)

            message = Message()

            if m.group(1):
                user_data = json.loads(m.group(1))
                message.author_name = user_data.get('full_name', '')
                message.author_picture = user_data.get('profile_pic_url', '')
                message.author_username = "@{}".format(user_data.get('username'))
            else:
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
