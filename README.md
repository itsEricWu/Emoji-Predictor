# Emoji-Predictor 🤖

Emojis are frequently employed in social media messages to enhance text-based communications with visual elements. In this study, we investigate the relationship between sentences and emojis, utilizing SOTA models to generate the most compatible emoji. Additionally, we examine the efficacy of large language models (LLMs) in generating and augmenting data. Our approach incorporates a range of NLP models, including Bidirectional Encoder Representations from Transformers (BERT), a pre-trained transformer model, a Support Vector Machine (SVM), a classic supervised learning technique, and Long Short-Term Memory (LSTM), a neural network-based learning model. Our experimental results demonstrate the successful prediction of compatible emojis from textual input, highlighting the potential of our approach in understanding emoji predicting and the feasible action for augmenting data by LLM.

We create a new Text to Emoji dataset by continuing prompting from GPT 3.5 turbo API with the tweet data sentiment140. The models are in the jupyter notebooks.
More about our finding can be found in [Exploring Emoji Prediction and Data Augmentation by GPT 3.5.pdf](https://github.com/itsEricWu/Emoji-Predictor/files/11391167/Exploring.Emoji.Prediction.and.Data.Augmentation.by.GPT.3.5.pdf)


There are two folder one for data generation and the other for data augmentation

The files in data generation pull raw text data from Twitter, then preprocess and use GPT 3.5 to label the data

The files in data augmentation randomly select text from emoji that have less than 200 samples, then use GPT 3.5 to generate related text for data augmentation🔧

Sample prediction from our model:

It is raining heavily outside. -----> 🌧

I am graduating from Purdue this May. ---------> 🎉

Heading home for a couple days----------->🏠
