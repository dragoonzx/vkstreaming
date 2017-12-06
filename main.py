# -*- coding: utf-8 -*-
from vkstreaming import Streaming


if __name__ == '__main__':
    api = Streaming("streaming.vk.com", "<key>")

    list = [{"tag":"Биткоин","value":'биткоин'},{"tag":"BTC","value":'btc'}, {"tag":"ETH","value":'eth'}, {"tag":"NEM","value":'nem'}]
    api.update_rules(list)
    
    rules = api.get_rules()
    for rule in rules:
        print(("{tag:15}:{value}").format(**rule))

    @api.stream
    def my_func(event):
        print("[{}]:[{}] {}".format(event['tags'], event['event_type'], event['event_url']))

api.start()
