import json
import numpy as np
import requests
def coin_em(rolls, theta_A=None, theta_B=None, maxiter=6):
    # Initial Guess
    theta_A = theta_A or random.random()
    theta_B = theta_B or random.random()
    thetas = [(theta_A, theta_B)]
    # Iterate
    for c in range(maxiter):
        print("#%d:\t%0.2f %0.2f" % (c, theta_A, theta_B))
        heads_A, tails_A, heads_B, tails_B = expect(rolls, theta_A, theta_B)
        theta_A, theta_B = maximize(heads_A, tails_A, heads_B, tails_B)
        
    thetas.append((theta_A,theta_B))    
    return thetas, (theta_A,theta_B)

def expect(rolls, theta_A, theta_B):
    heads_A, tails_A = 0,0
    heads_B, tails_B = 0,0
    for trial in rolls:
        likelihood_A = coin_likelihood(trial, theta_A)
        likelihood_B = coin_likelihood(trial, theta_B)
        Prob_A = likelihood_A / (likelihood_A + likelihood_B)
        Prob_B = likelihood_B / (likelihood_A + likelihood_B)
        heads_A += Prob_A * trial.count("1")
        tails_A += Prob_A * trial.count("0")
        heads_B += Prob_B * trial.count("1")
        tails_B += Prob_B * trial.count("0") 
    return heads_A, tails_A, heads_B, tails_B

def maximize(heads_A, tails_A, heads_B, tails_B):

    theta_A = heads_A / (heads_A + tails_A)
    theta_B = heads_B / (heads_B + tails_B)
    return theta_A, theta_B

def coin_likelihood(roll, bias):
    # P(X | Z, theta)
    numHeads = roll.count("1")
    flips = len(roll)
    return pow(bias, numHeads) * pow(1-bias, flips-numHeads)

rolls = []
for i in range(30):
    response = requests.get('https://urldefense.com/v3/__https://24zl01u3ff.execute-api.us-west-1.amazonaws.com/beta__;!!LIr3w8kk_Xxm!-mQDSGowby3T94YBEMuxvxQCH7DosYghRyAA-rd938URWYntehEd5S_9opyD$')
    json_data = response.json() if response and response.status_code == 200 else None
    rolls.append(''.join(str(e) for e in json.loads(json_data['body'])))

thetas, _ = coin_em(rolls, 0.6, 0.5, maxiter=6)