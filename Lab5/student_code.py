from __future__ import print_function
import math
import random

class Bayes_Classifier:

    def __init__(self):
        self.neg_r_total = 0
        self.pos_r_total = 0
        self.neg_w_total = 0
        self.pos_w_total = 0
        self.vocab_size = 0
        self.word_freq_neg = {}
        self.word_freq_pos = {}
        self.actual = []
        self.end_pos = 0
        self.end_neg = 0
        self.neg_denom = 0
        self.pos_denom = 0
        # stop words - idk if these are actually helpful.
        # could change to have stop words that are low difference??
        self.too_common = ['be', 'of', 'and', 'a', 'in',
        'that', 'have']
        return


    def count_freq(self, filename):
        with open(filename,'rt') as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n','')
            fields = line.split('|')
            wID = int(fields[0])
            sentiment = fields[1]
            self.actual.append(sentiment)
            if sentiment == '5':
                self.pos_r_total += 1
                words = fields[2].split()
                for w in words:
                    w = w.lower()
                    # self.pos_w_total += 1
                    if w in self.word_freq_pos:
                        self.word_freq_pos[w] += 1
                    else:
                        self.word_freq_pos[w] = 1
            else: # sentiment == '1'
                self.neg_r_total += 1
                words = fields[2].split()
                for w in words:
                    w = w.lower()
                    # self.neg_w_total += 1
                    if w in self.word_freq_neg:
                        self.word_freq_neg[w] += 1
                    else:
                        self.word_freq_neg[w] = 1
        # sum values of keys + unique words is denom for classify

        return

    def train(self,filename):
        # self.count_freq(filename)
        vocab = set()

        with open(filename,'rt') as f:
            lines = f.readlines()

        for line in lines:
            line = line.replace('\n','')
            fields = line.split('|')
            wID = int(fields[0])
            sentiment = fields[1]
            # words is a list of individual words in the review
            words = fields[2].split()
            if sentiment == '1':
                self.neg_r_total += 1
                for w in words:
                    w = w.lower()
                    self.neg_w_total += 1
                    vocab.add(w)
                    if w in self.word_freq_neg:
                        self.word_freq_neg[w] += 1
                    else:
                        self.word_freq_neg[w] = 1
            else:
                self.pos_r_total += 1
                for w in words:
                    w = w.lower()
                    vocab.add(w)
                    self.pos_w_total += 1
                    if w in self.word_freq_pos:
                        self.word_freq_pos[w] += 1
                    else:
                        self.word_freq_pos[w] = 1
        print(self.neg_r_total, self.pos_r_total)
        print(self.neg_w_total, self.pos_w_total)
        print(len(vocab))
        self.vocab_size = len(vocab)
        return

    def classify(self, filename):
        predict = []
        prob_pos_base = math.log(float(self.pos_r_total)/float(self.pos_r_total+self.neg_r_total))
        prob_neg_base = math.log(float(self.neg_r_total)/float(self.pos_r_total+self.neg_r_total))
        # print(prob_pos_base, prob_neg_base)
        with open(filename,'rt') as f:
            lines = f.readlines()

        for line in lines:
            line = line.replace('\n','')
            fields = line.split('|')
            wID = int(fields[0])
            sentiment = fields[1]
            words = fields[2].split()
            prob_pos = prob_pos_base
            prob_neg = prob_neg_base
            for w in words:
                w = w.lower()
                if w in self.word_freq_pos:
                    prob_pos += math.log(float(self.word_freq_pos[w]+1)/float(self.pos_w_total+self.vocab_size))
                    if w not in self.word_freq_neg:
                        prob_neg += math.log(float(1)/float(self.neg_w_total+self.vocab_size))
                if w in self.word_freq_neg:
                    prob_neg += math.log(float(self.word_freq_neg[w]+1)/float(self.neg_w_total+self.vocab_size))
                    if w not in self.word_freq_pos:
                        prob_pos += math.log(float(1)/float(self.pos_w_total+self.vocab_size))
            if prob_pos > prob_neg:
                classify = '5'
            else:
                classify = '1'
            predict.append(classify)
        return predict
    # def classify(self,filename):
    #     ap_cp = 0
    #     an_cp = 0
    #     ap_cn = 0
    #     an_cn = 0
    #     predict = []
    #     high_diff = []
    #     sum_key_pos = 0
    #     sum_key_neg = 0
    #     unique_words = set()
    #     for w in self.word_freq_pos:
    #         sum_key_pos += self.word_freq_pos[w]
    #         unique_words.add(w)
    #         # print('62', w, sum_key_pos)
    #     for w in self.word_freq_neg:
    #         sum_key_neg += self.word_freq_neg[w]
    #         # print('65', w, sum_key_neg)
    #         unique_words.add(w)
    #     # print('unique words is', len(unique_words))
    #     self.pos_denom = sum_key_pos + len(unique_words)
    #     self.neg_denom = sum_key_neg + len(unique_words)
    #     with open(filename,'rt') as f:
    #         lines = f.readlines()
    #     for line in lines:
    #         line = line.replace('\n','')
    #         fields = line.split('|')
    #         wID = int(fields[0])
    #         words = fields[2].split()
    #         prob_pos = math.log(float(self.pos_r_total)/float(self.pos_r_total+self.neg_r_total))
    #         prob_neg = math.log(float(self.neg_r_total)/float(self.pos_r_total+self.neg_r_total))
    #         # print(prob_neg, '98')
    #         # print(self.pos_r_total, '99')
    #         # print(self.neg_r_total, '100')
    #         for w in words:
    #             # print(w)
    #             w = w.lower()
    #             if w in self.word_freq_neg:
    #                 # print('in word_freq_neg')
    #                 prob_neg += math.log(float(self.word_freq_neg[w]+1)/float(self.neg_denom))
    #                 # print(self.neg_denom)
    #             if w in self.word_freq_pos:
    #                 prob_pos += math.log(float(self.word_freq_pos[w])/float(self.pos_denom))
    #
    #         if prob_pos > prob_neg:
    #             classify = '5'
    #         else:
    #             classify = '1'
    #
    #         if (fields[1] == '1') and (classify == '1'):
    #             an_cn += 1
    #         if (fields[1] == '1') and (classify == '5'):
    #             an_cp += 1
    #         if (fields[1] == '5') and (classify == '1'):
    #             ap_cn += 1
    #         if (fields[1] == '5') and (classify == '5'):
    #             ap_cp += 1
    #         predict.append(classify)
    #         # print(wID, classify)
    #
    #     print(an_cn, an_cp, ap_cn, ap_cp)
    #     # print(high_diff)
    #     # print(len(self.word_freq_neg))
    #     # print(len(high_diff))
    #     return predict
