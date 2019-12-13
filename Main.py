import Crawler
import WordCloud
import numpy as np
from PIL import Image
from wordcloud import WordCloud

alice_mask = np.array(Image.open("BackImg.png"))

wordcloud = WordCloud(
    font_path = font_path,
    width = 800,
    height = 800,
    background_color="white",
    mask = alice_mask
)

wordcloud = wordcloud.generate_from_frequencies(keywords)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()