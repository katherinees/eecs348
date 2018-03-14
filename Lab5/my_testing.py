import math
import sys
import student_code as nbc

bc = nbc.Bayes_Classifier()
bc.train('train.txt')
print sorted(bc.word_freq_neg, key = bc.word_freq_neg.get, reverse = True)
print bc.word_freq_pos['funny'], bc.pos_w_total
print bc.neg_r_total
bc.classify('train.txt')
# actual = []
# words_pos = []
# word_freq_pos = {}
# word_freq_neg = {}
# too_common = ['.', ',', 'the', 'movie', 'to', 'of', 'a', 'in', 'I', 'This',
#                 'of', 'is', 'this', 'as', 'at']
# pos_total = 0
# neg_total = 0
#
#
# with open('train.txt','rt') as f:
#     lines = f.readlines()
#
# for line in lines:
#     line = line.replace('\n','')
#     fields = line.split('|')
#     wID = int(fields[0])
#     sentiment = fields[1]
#     actual.append(sentiment)
#     if sentiment == '5':
#         pos_total += 1
#         # print fields[2]
#         words = fields[2].split()
#         for w in words:
#             if (w in too_common):
#                 break
#             if w in word_freq_pos:
#                 word_freq_pos[w] += 1
#             else:
#                 word_freq_pos[w] = 1
#     else: # sentiment == '1'
#         neg_total += 1
#         words = fields[2].split()
#         for w in words:
#             if (w in too_common):
#                 break
#             if w in word_freq_neg:
#                 word_freq_neg[w] += 1
#             else:
#                 word_freq_neg[w] = 1
#
# # print word_freq_pos
# # print word_freq_neg
# k = max(word_freq_pos, key = word_freq_pos.get)
# s = max(word_freq_neg, key = word_freq_neg.get)
# print 'most positive word', k, word_freq_pos[k]
# print 'pos reviews', pos_total
# print 'most negative word', s, word_freq_neg[s]
# print 'neg reviews', neg_total
# print 'neg', sorted(word_freq_neg, key = word_freq_neg.get, reverse = True)
# print 'pos', sorted(word_freq_pos, key = word_freq_pos.get, reverse = True)
