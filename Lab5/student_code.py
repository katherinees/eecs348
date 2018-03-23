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
        self.end_pos = 0
        self.end_neg = 0
        self.short_pos = 0
        self.short_neg = 0
        return

    def train(self,filename):
        vocab = set()
        pos_ave_l = []
        neg_ave_l = []

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
                neg_ave_l.append(len(words))
                if len(words) < 6:
                    self.short_neg += 1
                for w in words:
                    w = w.lower()
                    self.neg_w_total += 1
                    vocab.add(w)
                    if w in self.word_freq_neg:
                        self.word_freq_neg[w] += 1
                    else:
                        self.word_freq_neg[w] = 1
                if (len(words) > 1) and (words[-1] == '!'):
                    self.end_neg += 1
            else:
                self.pos_r_total += 1
                pos_ave_l.append(len(words))
                if len(words) < 6:
                    self.short_pos += 1
                for w in words:
                    w = w.lower()
                    vocab.add(w)
                    self.pos_w_total += 1
                    if w in self.word_freq_pos:
                        self.word_freq_pos[w] += 1
                    else:
                        self.word_freq_pos[w] = 1
                if (len(words) > 1) and (words[-1] == '!'):
                    self.end_pos += 1
        self.vocab_size = len(vocab)
        return

    def classify(self, filename):
        predict = []
        prob_pos_base = math.log(float(self.pos_r_total)/float(self.pos_r_total+self.neg_r_total))
        prob_neg_base = math.log(float(self.neg_r_total)/float(self.pos_r_total+self.neg_r_total))
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
            if (len(words) > 1) and (words[-1] == '!'):
                prob_pos += math.log(float(self.end_pos)/float(self.pos_r_total))
                prob_neg += math.log(float(self.end_neg)/float(self.neg_r_total))
            if (len(words) > 1) and (words[-1] != '!'):
                prob_pos += math.log(float(self.pos_r_total-self.end_pos)/float(self.pos_r_total))
                prob_neg += math.log(float(self.neg_r_total-self.end_neg)/float(self.neg_r_total))
            if (len(words) < 6):
                prob_pos += math.log(float(self.short_pos)/float(self.pos_r_total))
                prob_neg += math.log(float(self.short_neg)/float(self.neg_r_total))
            for w in words:
                w = w.lower()
                if w in self.word_freq_pos:
                    prob_pos += math.log(float(self.word_freq_pos[w]+1)/float(self.pos_w_total+self.vocab_size))
                    if w not in self.word_freq_neg:
                        prob_neg += math.log(float(2)/float(self.neg_w_total+self.vocab_size))
                if w in self.word_freq_neg:
                    prob_neg += math.log(float(self.word_freq_neg[w]+1)/float(self.neg_w_total+self.vocab_size))
                    if w not in self.word_freq_pos:
                        prob_pos += math.log(float(2)/float(self.pos_w_total+self.vocab_size))
            if prob_pos < prob_neg:
                classify = '1'
            else:
                classify = '5'
            predict.append(classify)
        return predict
