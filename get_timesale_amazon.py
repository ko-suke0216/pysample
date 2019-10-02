# endording UTF-8
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


def get_timesale():
    # URL
    URL = "https://www.amazon.co.jp/gp/goldbox?ref_=nav_cs_gb"

    # ヘッドレスモードを設定
    options = Options()
    #options.add_argument("--headless")

    # webdriverを設定
    CHROME_PATH = "C:\\work\\99_tool\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=CHROME_PATH, options=options)

    # htmlを取得
    driver.get(URL)
    driver.set_page_load_timeout(10)

    """
    # soupオブジェクトを作成
    soup = BeautifulSoup(driver.page_source, "lxml")

    # タイムセール商品を取得
    for hinmoku in soup.find_all("div", class_="a-section layer"):
        price = hinmoku.find("span", class_="a-size-medium inlineBlock unitLineHeight dealPriceText")
        product_name = hinmoku.find("a", class_="a-size-base a-link-normal dealTitleTwoLine singleCellTitle autoHeight")
        try:
            print(price.text.strip())
            print(product_name.text.strip())
            print(product_name.get("href").strip())
        except Exception as e:
            print(e)
    """
    # 次のページへ
    try:
        nextpage = driver.find_element_by_class_name("a-last").click()
        print(nextpage)
    except Exception as e:
        print(e)
    
    #wait = WebDriverWait(driver, 10)
    #elem = wait.until( expected_conditions.element_to_be_clickable( (By.CLASS_NAME, "a-last")))
    #nextpage = elem.click()

    # 終了
    driver.quit()

if __name__ == "__main__":

    get_timesale()