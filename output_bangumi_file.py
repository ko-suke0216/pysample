# coding: UTF-8
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime

def get_bangumi(file):
    # URL関連
    url = "https://www.home-tv.co.jp/programtable/"
 
    # ヘッドレスモードを設定
    options = Options()
    options.add_argument("--headless")
 
    # WebDriverを設定
    CHROME_PATH = "C:\\work\\99_tool\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=CHROME_PATH, options=options)
 
    # htmlを取得
    driver.get(url)
 
    # soupオブジェクトを作成
    soup = BeautifulSoup(driver.page_source, "lxml")
 
    # 番組情報を取得して日付、時刻、番組タイトル、番組概要を出力
    # 出力ディレクトリ
    now = datetime.datetime.now()
    output = "C:\\work\\02_Uipath\\" + "bangumi_{0:%Y%m%d%H%M%S}.txt".format(now)

    with open(output, mode="a") as f:
        for title in soup.find_all("li", attrs={"data-program": "番組枠"}):
            strdate = title.get("data-pagedate-hour")
            if strdate is not None:
                # 日付
                f.write("{}\n".format(strdate[0:8]))
            strtime = title.find("span", class_="time")
            if strtime is not None:
                # 時刻
                f.write("{}\n".format(strtime.text))
            strtitle = title.find("span", class_="title")
            if strtitle is not None:
                # 番組タイトル
                f.write("{}\n".format(strtitle.text))
            strdt = title.find("span", class_="dt ellipsis")
            if strdt is not None:
                # 番組概要
                f.write("{}\n".format(strdt.text))

    # Chromeドライバーを終了
    driver.close()

if __name__ == '__main__':
    #   # arguments
    #   argvs = sys.argv
    #   ## check
    #   if len(argvs) != 3:
    #       print("Usage: python scraping.py [url] [output]")
    #       exit()
    #   url = argvs[1]
    #   output_name = argvs[2]
    url = "https://www.home-tv.co.jp/programtable/"
    file = "bangumi.txt"

    get_bangumi(file)