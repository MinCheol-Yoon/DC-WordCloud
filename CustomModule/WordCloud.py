import Crawler
import WordCloud
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud

def WCGen():
    text = open("data.txt", encoding="utf-8").read()
    bg_mask = np.array(Image.open("BikeMask.jpg"))

    wc = WordCloud(background_color="white",
        font_path="NanumGothic.ttf",
        mask=bg_mask
    )

    wc = wc.generate(text)

    plt.figure(figsize=(12, 12))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()