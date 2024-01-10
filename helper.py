from urlextract import URLExtract
from wordcloud import WordCloud

extractor = URLExtract()

def fecth_stats(selected_user,df):


    if selected_user != "Overall":
        df = df[df["sender"] == selected_user]

    # Number of messages
    num_messages = df.shape[0]
    # numbers of words
    words = []
    for i in df["message"]:
        words.extend(i.split())

    # number of medias sended by user
    num_media_messgages = df[df['message'] == "<Media omitted>"].shape[0]

    # Number of links sended by user
    links = []
    for message in df["message"]:
        links.extend(extractor.find_urls(message))

    return num_messages , len(words) , num_media_messgages , len(links)

def most_busy_user(df):

    x = df["sender"].value_counts().head(5)

    df = round((df['sender'].value_counts() / df.shape[0]) * 100).reset_index().rename(columns={"count": "percent"})
    return x, df

def create_word_cloud(selected_user,df):

    if selected_user != "Overall":
        df = df[df["sender"] == selected_user]

    wc = WordCloud(width=300,height=300,min_font_size=10,background_color="white")
    def_c = wc.generate(df['message'].str.cat(sep= ' '))

    return  def_c



