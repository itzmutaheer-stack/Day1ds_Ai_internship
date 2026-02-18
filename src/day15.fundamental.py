# topic 1

favorable=1
total_outcomes=6
probability=favorable / total_outcomes

print("probability of rolling 4 on a fair die=",probability)
print("-"*50)

# independeny event example
p_rain =0.3
p_traffic=0.2
p_both = p_rain * p_traffic
print("Probability of Rain =", p_rain)
print("Probability of Traffic =", p_traffic)
print("Probability of both Rain AND Traffic =", p_both)
print("-" * 50)
   
# task 1
import random

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print(f"Experimental Probability of sum = 7: {experimental_probability}")

# task 2
import random

# ----------------------------
# 1. Independent Events
# Coin (Heads) AND Die (6)
# ----------------------------

P_heads = 1/2
P_six = 1/6

P_independent = P_heads * P_six

print("Independent Event Probability (Heads AND 6):", P_independent)


# ----------------------------
# 2. Dependent Events
# Two Red marbles without replacement
# ----------------------------

P_first_red = 5/10
P_second_red_given_first = 4/9

P_dependent = P_first_red * P_second_red_given_first

print("Dependent Event Probability (Two Reds without replacement):", P_dependent)


# ----------------------------
# 3. Simulation for Dependent Case
# ----------------------------

trials = 100000
success = 0

for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5
    first = random.choice(bag)
    bag.remove(first)
    second = random.choice(bag)

    if first == "R" and second == "R":
        success += 1

experimental_probability = success / trials

print("Experimental Probability (Simulation):", experimental_probability)

# task 3

# Given probabilities
P_spam = 0.1
P_ham = 0.9

P_free_given_spam = 0.9
P_free_given_ham = 0.05

# Step 1: Total probability of "Free"
P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

# Step 2: Bayes' Theorem
P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("P(Free) =", P_free)
print("P(Spam | Free) =", P_spam_given_free)
 