import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews

#提取特征函数
def extract_features(word_list):
    return dict([(word,True)for word in word_list])


if __name__=='__main__':
    positive_fileids=movie_reviews.fileids('pos')
    negative_fileids=movie_reviews.fileids('neg')
    #通过特征提取函数将语料库中的特征提取出来
    feature_positive=[(extract_features(movie_reviews.words(fileids=[f])),
                       'Positive')for f in positive_fileids]
    feature_negative=[(extract_features(movie_reviews.words(fileids=[f])),
                       'Negative')for f in negative_fileids]
    #将数据分为训练数据和测试数据
    threshold_factor=0.8
    threshold_positive=int(threshold_factor*len(feature_positive))
    threshold_nagetive=int(threshold_factor*len(feature_negative))
    feature_train=feature_positive[:threshold_positive]+feature_negative[:threshold_nagetive]
    feature_test=feature_positive[threshold_positive:]+feature_negative[threshold_nagetive:]
    #使用朴素贝叶斯分类器训练
    classifier=NaiveBayesClassifier.train(feature_train)
    print("\nAccuracy of the classifier:",nltk.classify.util.accuracy(classifier,feature_test))
    print("-------------------------------------------------------------")
    #获取对语义最有影响的前十个单词
    print("\Top 10 most information words:")
    for item in classifier.most_informative_features()[:10]:    print(item[0])
    print("-------------------------------------------------------------")
    #让我们来定义一些评论，用来测试分类器的效果
    input_reviews=["It is an amazing movie",     "This is a dull movie. I would never recommend it to anyone.",    "A complete and utter destruction of one of the most iconic superheroes. 0.1 effort and thought put into the storyline. A coming of age awkward teenage movie with a 'spiderman' stamp put on it. Bad jokes aimed at teenagers (at best). A complete caricature of a villain, a complete caricature of a Spiderman. Just please stop making this garbage Put some god damn effort! A total waste of time",    "Just staving off some negative reviews. Fits well into the Marvel movies to date and is an excellent follow up to Avengers: Endgame."]
    #来吧，让我们用训练好的分类器来预测这些文本的分类
    print("\nPredictions:")
    for review in input_reviews:
        print("\nReviews:",review)
        probdist=classifier.prob_classify(extract_features(review.split()))
        pred_sentiment=probdist.max()
        print("predicted sentiment:",pred_sentiment)#sentiment是情绪情感的意思哦
        print("probability:",round(probdist.prob(pred_sentiment),2))
