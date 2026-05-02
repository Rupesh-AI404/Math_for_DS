# Out of 1000 emails: 200 are spam

# Marginal probability = The chance of something happening by itself, ignoring everything else.


total   = 1000
spam    = 200

P_spam  = spam / total
print(f"P(spam)     = {P_spam}")      # 0.2  → 20% chance any email is spam
print(f"P(not spam) = {1 - P_spam}")  # 0.8  → always sums to 1.0
print(f"Odds(spam)  = {P_spam / (1 - P_spam):.2f}")  # 0.25 → 1:4 odds of spam vs not spam