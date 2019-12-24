import pandas as pd 
import numpy as np 

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns


def description_length(df):
    df["desc_length"]= df.description.str.split().str.len()
    return df

def one_word_one_cloud(words, title):
    plt.figure(figsize=(10, 6))
    cloud = WordCloud(background_color='white', width=1200, height=800).generate(words)

    plt.imshow(cloud)
    plt.title(title)
    plt.axis("off")
    plt.show()

def one_word_two_cloud(words1, words2, title1, title2):
    cloud1 = WordCloud(background_color='white', height=1600, width=1200).generate(words1)
    cloud2 = WordCloud(background_color='white', height=1600, width=1200).generate(words2)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.6, 0, .5, 1])]

    axs[0].imshow(cloud1)
    axs[1].imshow(cloud2)

    axs[0].set_title(title1)
    axs[1].set_title(title2)

    for ax in axs: ax.axis('off')


def two_word_one_cloud(words, title):
    data = {k[0] + ' ' + k[1]: v for k, v in words.to_dict().items()}
    cloud1= WordCloud(background_color='white', width=800, height=800).generate_from_frequencies(data)

    plt.figure(figsize=(10, 8))
    plt.imshow(cloud)
    plt.title(title)
    plt.axis("off")
    plt.show()


def two_word_two_cloud(words1, words2, title1, title2):
    data = {k[0] + ' ' + k[1]: v for k, v in words1.to_dict().items()}
    cloud1 = WordCloud(background_color='white', width=800, height=800).generate_from_frequencies(data)

    data = {k[0] + ' ' + k[1]: v for k, v in words2.to_dict().items()}
    cloud2 = WordCloud(background_color='white', width=800, height=800).generate_from_frequencies(data)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.6, 0, .5, 1])]

    axs[0].imshow(cloud1)
    axs[1].imshow(cloud2)

    axs[0].set_title(title1)
    axs[1].set_title(title2)

    for ax in axs: ax.axis('off')

def three_word_two_cloud(words1, words2, title1, title2):
    data = {k[0] + ' ' + k[1] + ' ' + k[2]: v for k, v in words1.to_dict().items()}
    cloud1 = WordCloud(background_color='white', width=1000, height=800).generate_from_frequencies(data)

    data = {k[0] + ' ' + k[1] + ' ' + k[2]: v for k, v in words2.to_dict().items()}
    cloud2 = WordCloud(background_color='white', width=1000, height=800).generate_from_frequencies(data)

    plt.figure(figsize=(10, 8))
    axs = [plt.axes([0, 0, .5, 1]), plt.axes([.6, 0, .5, 1])]

    axs[0].imshow(cloud1)
    axs[1].imshow(cloud2)

    axs[0].set_title(title1)
    axs[1].set_title(title2)

    for ax in axs: ax.axis('off')
