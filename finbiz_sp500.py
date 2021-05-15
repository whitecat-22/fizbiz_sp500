from IPython.display import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# ヘッドレスモードを指定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

#ここで、バージョンなどのチェックをします。
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = webdriver.Chrome(ChromeDriverManager().install())
# finvizのページへ遷移
url = "https://finviz.com/map.ashx?t=sec"
driver.get(url)

# 画面サイズの設定
driver.set_window_size(1920, 1080)

# ヒートマップの抽出
heatmap = driver.find_element_by_class_name("chart")

# スクショをバイナリーデータで取得
bf = heatmap.screenshot_as_png

driver.close()
driver.quit()

# 画像データとして保存する
with open("screenshot.png", "wb") as f:
    f.write(bf)
