import math
import sys
import student_code as nbc

def f_score(filename,predict):

    actual = []
    ids = []

    with open(filename,'rt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace('\n','')
        fields = line.split('|')
        wID = int(fields[0])
        ids.append(wID)
        sentiment = fields[1]
        actual.append(sentiment)

    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i in range(len(actual)):
        if predict[i] == '5' and actual[i] == '5':
            tp = tp + 1
        if predict[i] == '5' and actual[i] == '1':
            fp = fp + 1
            # print 'predicted 5 but actually 1', ids[i]
        if predict[i] == '1' and actual[i] == '1':
            tn = tn + 1
        if predict[i] == '1' and actual[i] == '5':
            fn = fn + 1
            # print 'predicted 1 but actually 5', ids[i]

    precision = float(tp)/float(tp+fp)
    recall = float(tp)/float(tp+fn)
    f_score = float(2.0)*precision*recall/(precision+recall)

    return(f_score)

bc1 = nbc.Bayes_Classifier()
bc1.train('train_short.txt')
predict = bc1.classify('halfA.txt')
fA = f_score('answershalfA.txt',predict)
print 'less skew data f score is', fA

# bc2 = nbc.Bayes_Classifier()
# bc2.train_improve('train_short.txt')
# predict = bc2.classify_improve('halfA.txt')
# fA = f_score('answershalfA.txt',predict)
# print 'less skew improved?  f is', fA

bc3 = nbc.Bayes_Classifier()
bc3.train('train.txt')
predict = bc3.classify('classifyA.txt')
fA = f_score('answersA.txt',predict)
print 'more skew data f score is', fA

# bc4 = nbc.Bayes_Classifier()
# bc4.train_improve('train.txt')
# predict = bc4.classify_improve('classifyA.txt')
# fA = f_score('answersA.txt',predict)
# print 'more skew improves?  f is', fA

# 'sses' stem no change ls, slight hurt ms
# '!' never seems to help??? feel like it should
