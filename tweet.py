# -*- coding: utf-8 -*-

import sys
import oauth2 as oauth
from urllib import urlencode


def hasError(param):
    '''
    ガード節
    '''
    if len(param) == 1:
        print u'引数にツイート内容を渡してちょ！'
        return True
    if not param[1]:
        print u'空ツイートはさせませんよ！'
        return True
    return False


def tweet():
    '''
    ツイートする
    '''
    # Tweet内容を取得します
    tweet = unicode(param[1], 'utf-8')
    print u'ツイート内容：' + tweet

    # Twitter接続情報をセットします
    consumer_key = ""
    consumer_secret = ""
    access_token_key = ""
    access_token_secret = ""

    client = oauth.Client(
        oauth.Consumer(key=consumer_key, secret=consumer_secret),
        oauth.Token(key=access_token_key, secret=access_token_secret)
    )

    # TwitterにPOSTする
    client.request(
        'https://api.twitter.com/1.1/statuses/update.json',
        'POST',
        urlencode({
            'status': tweet.encode('utf-8')
        }),
    )

if __name__ == '__main__':
    '''
    Main
    '''
    # コマンドライン引数を取得します
    param = sys.argv

    # ガード節
    if hasError(param):
        sys.exit()

    tweet()
