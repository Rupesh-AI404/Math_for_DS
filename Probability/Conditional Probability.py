# P(spam | email contains "free")
# = out of ALL emails with "free", what fraction are spam?

P_free_given_spam = 0.40  # 40% of spam has "free"
P_spam            = 0.20
P_free            = 0.10

# Definition of conditional probability:
P_spam_given_free = (P_free_given_spam * P_spam) / P_free
print(f"P(spam | contains 'free') = {P_spam_given_free}")  # 0.80

# Knowing the email has "free" → 80% chance it's spam!
# Direction of condition completely changes the answer