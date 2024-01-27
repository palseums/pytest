from urllib import request

URL = "https://facebook.com"




def fetch_net():
    '''1. get data from www'''
    #response = request.urlopen(URL,)
    if URL == URL:
        return "abc"
    return "bcd"


def parse():
    answer = fetch_net() + str(123)
    return answer


print(parse())
