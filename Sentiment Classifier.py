punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(st):
    for s in st:
        if s in punctuation_chars:
            st = st.replace(s,'')
    return st

def get_pos(st):
    pun = strip_punctuation(st)
    starray = (pun.lower().split())
    count = 0
    for s in starray:
        if s in positive_words:
            count += 1
    return count

def get_neg(st):
    pun = strip_punctuation(st)
    starray = (pun.lower().split())
    count = 0
    for s in starray:
        if s in negative_words:
            count += 1
    return count

def readandwrite():
    fileread = open("project_twitter_data.csv","r")
    filewrite = open("resulting_data.csv","w")

    lines =  fileread.readlines()
    lines.pop(0)

    filewrite.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    filewrite.write("\n")

    for line in lines:
        lis = line.strip().split(',')
        tweet = lis[0]
        retweets = lis[1]
        replies = lis[2]
        positives = get_pos(tweet)
        negatives = get_neg(tweet)
        netscore = positives - negatives
        filewrite.write("{}, {}, {}, {}, {}".format(retweets,replies,positives,negatives,netscore))
        filewrite.write("\n")
    fileread.close()
    filewrite.close()

readandwrite()
