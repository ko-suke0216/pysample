# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

# アクセスするURL
url = "http://www.nikkei.com/markets/kabu/"

# URL にアクセスする
html = urllib2.urlopen(url)

# html を BeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# span要素全てを摘出する　→　全てのspa要素が配列に入って返される
span = soup.find_all("span")

# print時のエラーとならないように最初に宣言しておきます。
nikkei_heikin = ""

# for文で全てのspan要素から Class="mkc-stock_prices"となっているものを探します
for tag in span:
    # calssの設定がされていない要素は、tag.get("class").pop(0)を行うことができないでエラーとなるため、tryで回避する
    try:
        # tag の中からclass="n"のnの文字列を摘出します。複数classが設定されている場合があるので
        # get関数では配列で帰ってくる。そのため配列の関数pop(0)により、配列の一番最初を摘出する
        # <span class="hoge" class="foo">  →　　["hoge", "foo"]  →　hoge
        string_ = tag.get("class").pop(0)

        # 摘出したclassの文字列にmkc-stock_prices と設定されているかを調べます
        if string_ in "mkc-stock_prices":
            # mkc-stock_prices が設定されているのでtagで囲まれた文字列を.stringであぶり出します
            nikkei_heikin = tag.string
            # 摘出が完了したのでfor文を抜けます
            break
    except:
        # パス　→　何も処理を行わない
        pass

# 日経平均株価
print nikkei_heikin