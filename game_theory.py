# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 18:44:23 2019

Game Theory: Prisoner's Dilemma

@author: rayde
"""


players = ["Bill", "John"]
strategies = ['cooperate','defect']
actions = []
types = []
beliefs = []
utilities = []

arguments = [players, actions, strategies, types, beliefs, utilities]

bill_actions = [{motivated:2}, {unmotivated:1}]
john_actions = [{motivated:1}, {unmotivated:0}]

def Bill(p1_strategy, p2_strategy, types, beliefs):
    if p1_strategy == 'cooperate' and p2_strategy == 'cooperate':
        payoff = 4
    if p1_strategy == 'cooperate' and p2_strategy == 'defect':
        payoff = 0
    if p1_strategy == 'defect' and p2_strategy == 'cooperate':
        payoff = 5
    if p1_strategy == 'defect' and p2_strategy == 'defect':
        payoff = 1
    return payoff

def John(p1_strategy, p2_strategy, types, beliefs):
    if p1_strategy == 'cooperate' and p2_strategy == 'cooperate':
        payoff = 4
    if p1_strategy == 'cooperate' and p2_strategy == 'defect':
        payoff = 5
    if p1_strategy == 'defect' and p2_strategy == 'cooperate':
        payoff = 0
    if p1_strategy == 'defect' and p2_strategy == 'defect':
        payoff = 1
    return payoff

Bill = Bill('cooperate', 'defect')
John = John('cooperate', 'defect')
