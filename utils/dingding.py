from dingtalkchatbot.chatbot import DingtalkChatbot

from django.conf import settings


def send(message, at_modiles=None):
    """
        给钉钉群发送群消息并且@别人,需要注意的是
        该webhook添加方式使用的是关键词的方式，因此发送消息的时候，需要包含指定的关键词(通知)
    :param message: 需要发送的消息
    :param at_modiles: 需要@的人的列表list，列表中是手机号
    :return: None
    """
    webhook = settings.DINGDING_WEBHOOK

    dingding = DingtalkChatbot(webhook=webhook)

    at_modiles = at_modiles if at_modiles else []

    dingding.send_text(message, at_mobiles=at_modiles)


if __name__ == '__main__':
    send(message='通知:这个是测试消息')
