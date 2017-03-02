from social.models import Message


class Provider(object):

    def __init__(self, provider):
        self.provider = provider

    # noinspection PyMethodMayBeStatic
    def get_recent_messages(self, feed, **kwargs):
        """
        Get recent messages posted on this provider
        :return: List of message to add into database
        :rtype: Message
        """
        last_id = feed.messages.filter(providers=(self.provider,)).last().provider_post_id
        return []
