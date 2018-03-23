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
        # stop words - idk if these are actually helpful.
        # could change to have stop words that are low difference??
        self.too_common = []
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
                for w in words:
                    if w not in self.too_common:
                        w = w.lower()
                        # if w.endswith('sses'):
                        #     w = w[:len(w)-2]
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
                for w in words:
                    if w not in self.too_common:
                        w = w.lower()
                        # if w.endswith('sses'):
                        #     w = w[:len(w)-2]
                        vocab.add(w)
                        self.pos_w_total += 1
                        if w in self.word_freq_pos:
                            self.word_freq_pos[w] += 1
                        else:
                            self.word_freq_pos[w] = 1
                if (len(words) > 1) and (words[-1] == '!'):
                    self.end_pos += 1
        # print(self.neg_r_total, self.pos_r_total)
        # print(self.neg_w_total, self.pos_w_total)
        # print(len(vocab))
        # print('hypothesis', self.end_pos, self.end_neg)
        # print('does length matter', float(self.pos_w_total/self.pos_r_total), float(self.neg_w_total/self.neg_r_total))
        self.vocab_size = len(vocab)
        return

    def classify(self, filename):
        predict = []
        high_diff = []
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
            # if (len(words) > 55):
            #     prob_pos += math.log(float(1)/float(self.pos_r_total))
            # if (len(words) < 46):
            #     prob_neg += math.log(float(1)/float(self.neg_r_total))
            # if (len(words) > 1) and (words[-1] == '!'):
            #     prob_pos += math.log(float(self.end_pos)/float(self.pos_r_total))
            #     prob_neg += math.log(float(self.end_neg)/float(self.neg_r_total))
            # if (len(words) > 1) and (words[-1] != '!'):
            #     prob_pos += math.log(float(self.pos_r_total-self.end_pos)/float(self.pos_r_total))
            #     prob_neg += math.log(float(self.neg_r_total-self.end_neg)/float(self.neg_r_total))
            for w in words:
                w = w.lower()
                if w not in self.too_common:
                    # if w.endswith('sses'):
                    #     w = w[:len(w)-2]
                    if w in self.word_freq_pos:
                        prob_pos += math.log(float(self.word_freq_pos[w]+1)/float(self.pos_w_total+self.vocab_size))
                        if w not in self.word_freq_neg:
                            prob_neg += math.log(float(2)/float(self.neg_w_total+self.vocab_size))
                    if w in self.word_freq_neg:
                        prob_neg += math.log(float(self.word_freq_neg[w]+1)/float(self.neg_w_total+self.vocab_size))
                        if w not in self.word_freq_pos:
                            prob_pos += math.log(float(2)/float(self.pos_w_total+self.vocab_size))
                    if (w in self.word_freq_pos) and (w in self.word_freq_neg):
                        if abs(math.log(float(self.word_freq_pos[w]+1)/float(self.pos_w_total+self.vocab_size)) - math.log(float(self.word_freq_neg[w]+1)/float(self.neg_w_total+self.vocab_size)) < 0.0001):
                            if w not in high_diff:
                                high_diff.append(w)
            if prob_pos < prob_neg:
                classify = '1'
            else:
                classify = '5'
            predict.append(classify)
        # print(high_diff)
        return predict

    def train_improve(self,filename):
        # self.count_freq(filename)
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
                    if w not in self.too_common:
                        w = w.lower()
                        # if w.endswith('sses'):
                        #     w = w[:len(w)-2]
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
                    if w not in self.too_common:
                        w = w.lower()
                        # if w.endswith('sses'):
                        #     w = w[:len(w)-2]
                        vocab.add(w)
                        self.pos_w_total += 1
                        if w in self.word_freq_pos:
                            self.word_freq_pos[w] += 1
                        else:
                            self.word_freq_pos[w] = 1
                if (len(words) > 1) and (words[-1] == '!'):
                    self.end_pos += 1
        # print(self.neg_r_total, self.pos_r_total)
        # print(self.neg_w_total, self.pos_w_total)
        # print(len(vocab))
        # print('hypothesis', self.end_pos, self.end_neg)
        # print('does length matter', float(self.pos_w_total/self.pos_r_total), float(self.neg_w_total/self.neg_r_total))
        pos_mean = self.pos_w_total/self.pos_r_total
        neg_mean = self.neg_w_total/self.neg_r_total
        pos_above_p_ave = 0
        pos_less_n_ave = 0
        neg_above_p_ave = 0
        neg_less_n_ave = 0
        for l in pos_ave_l:
            if l > pos_mean:
                pos_above_p_ave += 1
            if l < neg_mean:
                pos_less_n_ave += 1
        for l in neg_ave_l:
            if l > pos_mean:
                neg_above_p_ave += 1
            if l < neg_mean:
                neg_less_n_ave += 1
        # TRYING TO DO LENGTH STUFF I THINK UNHELPFUL??
        # print(pos_mean, neg_mean)
        # print(pos_ave_l)
        # print(neg_ave_l)
        # print(pos_above_p_ave, pos_less_n_ave, neg_above_p_ave, neg_less_n_ave)
        # print(self.short_pos, self.pos_r_total)
        # print(self.short_neg, self.neg_r_total)
        self.vocab_size = len(vocab)
        return

    def classify_improve(self, filename):
        predict = []
        high_diff = []
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
            # if (len(words) > 55):
            #     prob_pos += math.log(float(1)/float(self.pos_r_total))
            # if (len(words) < 46):
            #     prob_neg += math.log(float(1)/float(self.neg_r_total))
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
                if w not in self.too_common:
                    # if w.endswith('sses'):
                    #     w = w[:len(w)-2]
                    if w in self.word_freq_pos:
                        prob_pos += math.log(float(self.word_freq_pos[w]+1)/float(self.pos_w_total+self.vocab_size))
                        if w not in self.word_freq_neg:
                            prob_neg += math.log(float(2)/float(self.neg_w_total+self.vocab_size))
                    if w in self.word_freq_neg:
                        prob_neg += math.log(float(self.word_freq_neg[w]+1)/float(self.neg_w_total+self.vocab_size))
                        if w not in self.word_freq_pos:
                            prob_pos += math.log(float(2)/float(self.pos_w_total+self.vocab_size))
                    if (w in self.word_freq_pos) and (w in self.word_freq_neg):
                        if abs(math.log(float(self.word_freq_pos[w]+1)/float(self.pos_w_total+self.vocab_size)) - math.log(float(self.word_freq_neg[w]+1)/float(self.neg_w_total+self.vocab_size)) < 0.0001):
                            if w not in high_diff:
                                high_diff.append(w)
            if prob_pos < prob_neg:
                classify = '1'
            else:
                classify = '5'
            predict.append(classify)
        # print(high_diff)
        return predict
