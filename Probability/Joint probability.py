# P(spam AND contains word "free")
P_spam        = 0.20
P_free        = 0.10   # 10% of all emails contain "free"

# If independent: multiply
P_spam_and_free = P_spam * P_free
print(f"P(spam AND free) = {P_spam_and_free}")  # 0.02

# But if dependent — use conditional instead:
P_free_given_spam = 0.40   # 40% of spam emails contain "free"
P_spam_and_free   = P_free_given_spam * P_spam
print(f"P(spam AND free) = {P_spam_and_free}")  # 0.08  ← correct way