from __future__ import print_function
import math
import random

class Bayes_Classifier:

    def __init__(self):
        self.neg_r_total = 0
        self.pos_r_total = 0
        self.neg_w_total = 0
        self.pos_w_total = 0
        self.word_freq_neg = {}
        self.word_freq_pos = {}
        self.actual = []
        self.end_pos = 0
        self.end_neg = 0
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
                # print type(words)
                # print(len(words))
                if (len(words) > 1) and (words[-1] == '!'):
                    self.end_pos += 1
                    # print(end_pos)
                for w in words:
                    w = w.lower()
                    if w not in self.too_common:
                        if w.endswith('ly'):
                            # print(w)
                            w = w[:len(w)-2]
                            # print(w)
                        # if w.endswith('ed'):
                        #     print(w)
                        #     w = w[:len(w)-2]
                        #     print(w)
                        # if w.endswith('s'):
                        #     print(w)
                        #     w = w[:len(w)-1]
                        #     print(w)
                        # if w.endswith('ing'):
                        #     print(w)
                        #     w = w[:len(w)-3]
                        #     print(w)
                        self.pos_w_total += 1
                        if w in self.word_freq_pos:
                            self.word_freq_pos[w] += 1
                        else:
                            self.word_freq_pos[w] = 1
            else: # sentiment == '1'
                self.neg_r_total += 1
                words = fields[2].split()
                if (len(words) > 1) and (words[-1] == '!'):
                    self.end_neg += 1
                for w in words:
                    w = w.lower()
                    if w not in self.too_common:
                        if w.endswith('ly'):
                            # print(w)
                            w = w[:len(w)-2]
                            # print(w)
                        # if w.endswith('ed'):
                        #     print(w)
                        #     w = w[:len(w)-2]
                        #     print(w)
                        # if w.endswith('s'):
                        #     print(w)
                        #     w = w[:len(w)-1]
                        #     print(w)
                        # if w.endswith('ing'):
                        #     print(w)
                        #     w = w[:len(w)-3]
                        #     print(w)
                        self.neg_w_total += 1
                        if w in self.word_freq_neg:
                            self.word_freq_neg[w] += 1
                        else:
                            self.word_freq_neg[w] = 1
        print('hypothesis', self.end_pos, self.end_neg)
        h_pos = float(self.end_pos)/float(self.pos_r_total)
        h_neg = float(self.end_neg)/float(self.neg_r_total)
        print('does it', h_pos, h_neg)
        # +1 smoothing or something lol
        # if using train_eq, change all to 0.1 is best
        for w in self.word_freq_neg:
            self.word_freq_neg[w] += 1
        for w in self.word_freq_pos:
            self.word_freq_pos[w] += 1
        for w in self.word_freq_neg:
            if w not in self.word_freq_pos:
                self.word_freq_pos[w] = 1
        for w in self.word_freq_pos:
            if w not in self.word_freq_neg:
                self.word_freq_neg[w] = 1
        return

    def calc_prob(self, filename):

        return

    def train(self,filename):
        self.count_freq(filename)
        return


    def classify(self,filename):
        ap_cp = 0
        an_cp = 0
        ap_cn = 0
        an_cn = 0
        predict = []
        high_diff = []
        with open(filename,'rt') as f:
            lines = f.readlines()
        for line in lines:
            line = line.replace('\n','')
            fields = line.split('|')
            wID = int(fields[0])
            words = fields[2].split()
            prob_pos = math.log(float(self.pos_w_total)/float(self.pos_w_total+self.neg_w_total))
            prob_neg = math.log(float(self.neg_w_total)/float(self.pos_w_total+self.neg_w_total))
            for w in words:
                w = w.lower()
                if w.endswith('ly'):
                    # print(w)
                    w = w[:len(w)-2]
                    # print(w)
                # if w.endswith('ed'):
                #     print(w)
                #     w = w[:len(w)-2]
                #     print(w)
                # if w.endswith('s'):
                #     print(w)
                #     w = w[:len(w)-1]
                #     print(w)
                # if w.endswith('ing'):
                #     print(w)
                #     w = w[:len(w)-3]
                #     print(w)
                if w in self.word_freq_neg:
                    prob_neg += math.log(float(self.word_freq_neg[w])/float(self.neg_w_total))
                if w in self.word_freq_pos:
                    prob_pos += math.log(float(self.word_freq_pos[w])/float(self.pos_w_total))
                    # trying to figure out some high difference stuff:
                    if abs((100*float(self.word_freq_neg[w])/float(self.neg_w_total)-100*float(self.word_freq_pos[w])/float(self.pos_w_total)))>0.1:
                        if w not in high_diff:
                            high_diff.append(w)

            if prob_pos > prob_neg:
                classify = '5'
            else:
                classify = '1'

            if (fields[1] == '1') and (classify == '1'):
                an_cn += 1
            if (fields[1] == '1') and (classify == '5'):
                an_cp += 1
            if (fields[1] == '5') and (classify == '1'):
                ap_cn += 1
            if (fields[1] == '5') and (classify == '5'):
                ap_cp += 1
            predict.append(classify)
            # print(wID, classify)

        print(an_cn, an_cp, ap_cn, ap_cp)
        print(high_diff)
        print(len(self.word_freq_neg))
        print(len(high_diff))
        return predict
