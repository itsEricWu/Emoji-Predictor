import pandas as pd
import numpy as np
import re


def preprocess(text):
    # Replace repeated punctuation signs with labels and add spaces
    text = re.sub(r'(\.{2,})', r' multistop ', text)
    text = re.sub(r'(\!{2,})', r' multiexclamation ', text)
    text = re.sub(r'(\?{2,})', r' multiquestion ', text)
    # Add spaces before and after single punctuation signs
    text = re.sub(r'(\.|\!|\?|\,)', r' ', text)
    return text
def load_emoticons(emo_filename):
    # Load emoticons and their polarity from a file
    emoticon_dict = {}
    with open(emo_filename, 'r', encoding='latin-1') as file:
        for line in file:
            emoticon, polarity = line.strip().split('\t')
            emoticon_dict[emoticon] = polarity
    return emoticon_dict

# Load emoticons and their polarity from a file
emoticon_dict = load_emoticons('EmoticonLookupTable.txt')

def replace_emoticons(text, emoticon_dict=emoticon_dict):
    # Replace emoticons with their polarity and delete neutral ones
    for emoticon, polarity in emoticon_dict.items():
        pattern = re.compile(re.escape(emoticon), re.IGNORECASE)
        if polarity == '1':
            text = pattern.sub("positive", text)
        elif polarity == '-1':
            text = pattern.sub("negative", text)
        else:
            text = pattern.sub('', text)
            
    text = re.sub(r'[^a-zA-Z\s]', '', text)
            
    return text.split()
np.random.seed(42)

df = pd.read_csv("tweets.csv",encoding = "latin",header=None)
df = df.sample(100000)
df = df.iloc[:,[5,0]]
df.columns = ['text','class']
# df['class'][df['class']==4] = 1
df = df.reset_index(drop=True)
df["text"] = df["text"].apply(preprocess)
df["text"] = df["text"].apply(replace_emoticons)
df["text"] = df["text"].apply(lambda x: " ".join(x))
df.to_csv('tweets111.csv')
    


