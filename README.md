# Estimating-parameters-for-a-simple-model-using-the- expectation–maximization (EM)-algorithm
Estimate parameters for a simple model using the EM algorithm: What are the chances of heads and tails from two unlabeled coins? To figure it out I have implemented an EM algorithm that estimates the probability of heads for two coins using data from an API.


Development of my algorithm

We have been asked to estimate the theta parameters for the two coins based on the draws returned from the API.
It is fairly simple to access the API and get the values for each draw. This can be done as follows:
1.	Import json and import requests
2.	Get a response from the given API link using requests.get()
3.	Parse the json using json_data[‘body’] and append  it to a list
4.	The above process will be done 30 times since we have been asked to take a set of 30 coin flip draws
After performing first 4 steps, we would then have a list containing all the 30 coin flip draws and each draw consisting of 20 flips.
Let us suppose that we are given 2 coins and each time we are flipping a coin (we know) n times and calculating the theta values for that coin (in the end) based on the number of heads and tails (no of heads of coinA/ (no of heads of coinA + no of tails of coinB)). We can calculate these theta values if we know which coin we have flipped.  But what if we are just given the values of a coin flip and are not aware which coin was flipped which time? How can we calculate the theta values if we don’t know which coin was flipped which time? Can we guess the percentage of heads that each coin yields?  To do so we need to use the EM algorithm. We will follow the below steps to calculate the final theta values.
Step1: In the beginning since we don’t have any initial theta values for the 2 coins we can randomly assign some theta values.
Step2: We will be performing some n iterations. This n is not a fixed number but a value after which the theta values converge. In each iteration we will be doing following:
1.	Calculating the likelihood of getting a head from coin A and coin B. This is given by 
pow(theta, numHeads) * pow(1-theta, flips-numHeads) where theta will be thetaA and thetaB and numHeads is number of 1’s in that trial.
2.	Next step is to calculate the probability of both the coins. This can be done by normalizing the likelihood we calculated in step1.
ProbA=likelihoodA/(likelihoodA+likelihoodB)
ProbB=likelihoodB/(likelihoodA+likelihoodB)
3.	Now that we have the probability, we can find the number of heads and number of tails for each of the coins.
Number_heads_of_A += Prob A * number of heads in that trial (where heads will be 1 in our case)
Number_tails_of_A += Prob A * number of tails in that trial  
Number_heads_of_B+ = Prob B * number of heads in that trial (where heads will be 1 in our case)
Number_tails_of_B+ = Prob B * number of tails in that trial  
4.	Now that we have number of heads and tails for each coin we can calculate theta:
    theta_A = heads_A / (heads_A + tails_A)
    theta_B = heads_B / (heads_B + tails_B)
This will be the maximizing step 
5.	Now we will use this theta_A and theta_B in place of random values we had given initially and continue step 2 till convergence.

3.1.   What is your estimate of the thetas for the two coins?
  The estimate of theta will vary depending upon the intial values chosen and may also be different due to the randomness for each coin draw. I have chosen the random values as that given in the research paper (0.6, 0.5). Using this my estimate of thetas is as below for 6 iterations. After 6 iterations, I found that value starts converging which is why my no of iterations is 6. Below is one of my estimates:
#0:	0.60 0.50
#1:	0.60 0.35
#2:	0.64 0.30
#3:	0.65 0.30
#4:	0.65 0.30
#5:	0.65 0.30
3.2.   What choices did you have to make in writing your code? What options were available and why did you choose the option you implemented?
As mentioned above:
I had to make the choices of choosing initial theta values and also the number of iterations. The choice of initial theta values is random. But I decided to stop at 6 iterations since after 6 iterations; I observed that value started converging. 



