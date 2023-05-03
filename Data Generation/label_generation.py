import openai
import pandas as pd
import tqdm
openai.organization = "org-rSBOy4Zvb2tJ9HIPGEWY43UT"
openai.api_key = "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"
def get_emoji_based_on_text(text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"I would like you to be a predictive tool that provides an emoji based on a given text's tone, emotion, feeling, or character. Your task is to predict the most suitable emoji that matches the meaning of the text, and simply provide only one emoji as the output.\n\nText: {text}\n\nEmoji:",
            temperature=0.2,  # Lower temperature for more deterministic output
            max_tokens=3,  # Limit max tokens to reduce response length
            top_p=1,
            frequency_penalty=0.8,  # Increase frequency penalty to suppress common tokens
            presence_penalty=0.8  # Increase presence penalty to suppress recently mentioned tokens
        )
        emoji = response['choices'][0]['text'].strip()
        return emoji
    except Exception as e:
        print(e)
        return ""
s = pd.read_csv("tweets_preprocess.csv")
result = pd.DataFrame()
result['text'] = s['text']
b = open("tweets_preprocess_emoji.csv", "a", encoding="utf-8")
for i in tqdm.tqdm(range(0,36175)):
    temp1 = result.loc[i, 'text']
    temp = get_emoji_based_on_text(temp1)
    b.write(temp1+", "+temp + "\n")
b.close()

