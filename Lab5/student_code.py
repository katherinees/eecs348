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
        self.too_common = ['.', ',', 'the', 'movie', 'to', 'of', 'a', 'in', 'I', 'This',
                        'of', 'is', 'this', 'as', 'at']
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
                # print fields[2]
                words = fields[2].split()
                # words = list(set(words))
                for w in words:
                    self.pos_w_total += 1
                    # if (w in self.too_common):
                    #     break
                    if w in self.word_freq_pos:
                        self.word_freq_pos[w] += 1
                    else:
                        self.word_freq_pos[w] = 1
            else: # sentiment == '1'
                self.neg_r_total += 1
                words = fields[2].split()
                for w in words:
                    self.neg_w_total += 1
                    # if (w in self.too_common):
                    #     break
                    if w in self.word_freq_neg:
                        self.word_freq_neg[w] += 1
                    else:
                        self.word_freq_neg[w] = 1
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
                # print(w)
                if w in self.word_freq_neg:
                    # print('what is frequency')
                    # print(self.word_freq_neg[w])
                    # print('what is total')
                    # print(self.neg_r_total)
                    # print(float(self.word_freq_neg[w])/float(self.neg_w_total))
                    prob_neg += math.log(float(self.word_freq_neg[w])/float(self.neg_w_total))
                # elif w not in self.word_freq_neg:
                    # term_neg = math.log(float(1)/float(self.neg_w_total))
                # prob_neg += term_neg
                if w in self.word_freq_pos:
                    prob_pos += math.log(float(self.word_freq_pos[w])/float(self.pos_w_total))
                # elif w not in self.word_freq_pos:
                    # term_pos = math.log(float(1)/float(self.pos_w_total))
                # prob_pos += term_pos
            # print(words)
            # if actuallly negative and we class as neg
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
            print(wID, classify)

        print(an_cn, an_cp, ap_cn, ap_cp)
        return predict
