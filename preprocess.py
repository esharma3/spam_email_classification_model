import re
import time
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


###########################################################################################
#                            PREPARING DATA FOR PREDICTION                                #
###########################################################################################


def lemmitize(s):
    lemmatizer = WordNetLemmatizer()
    new_s = ""
    for word in s.split(" "):
        lemmatizer.lemmatize(word)
        if word not in stopwords.words("english"):
            new_s += word + " "
    return new_s[:-1]


def clean_str(s):
    # make everything lowercase
    s = s.lower()
    # remove urls
    s = re.sub(re.compile(r"https?:\/\/(www)?.?([A-Za-z_0-9-]+)([\S])*"), "", s)
    # remove emails
    s = re.sub(re.compile(r"\S+@\S+"), "", s)
    # remove punctuation
    s = re.sub(re.compile(r"[^a-z\s]"), "", s)
    return s


def prep_data(s):
    clean_data = clean_str(s)
    clean_text = lemmitize(clean_data)
    d = {"clean_text": clean_text}
    return pd.DataFrame([d])



###########################################################################################
#                                        MAIN                                             #
###########################################################################################

if __name__ == "__main__":
    t = time.time()
    string = "That somehow managed to be record short yet answer almost all the questions we would've asked, haha! Hi Deb! Welcome to Hou Tian; nice to meet you! I'm Jhenne, one of the mods here-- which means I gotta give you the modly speech :] Make sure to check out the Mandatory Reading up top! Our constantly updated Library is also a great resource, though it isn't mandatory reading-- we like to tell members to 'read as you need', rather than marathon read it all at once. One of the most helpful threads is the Gameplay So Far thread, which breaks down what all has gone down on the boards. (Now, the summary for January isn't tossed up yet, but we'd be happy to break down what you missed if you'd like.) I see that you're interested in Mai! That means both the Trying for a Canon Character page, and the Canon Character Rules and Consequences post will be helpful to check out. If you're ever considering an original character, we have our player-made adoptables list, and our factions, comprised of the Jade Shark/Bending Opposition, Original People of the Flame, and The Bending Crime Syndicates. As far as characters go, in the past tense I play Srai, a Jade Shark [s]that is very very dusty. In the Korraverse I play a reporter named Chihiro, and an ex-taxi dancer/wannabe actress named Naoki, and a Republic City University student named Haruna. I think that's it! If you have any questions, don't hesitate to ask a mod, or drop it right here in this thread so we can get back to you! Again, welcome! #CONFETTI"
    print(string)
    print(prep_data(string))
    print(f"Preprocessing Time: {time.time() - t} seconds")
