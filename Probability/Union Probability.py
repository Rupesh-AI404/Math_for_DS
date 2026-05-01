# P(email is spam OR contains "free")
P_spam          = 0.20
P_free          = 0.10
P_spam_and_free = 0.08   # from above

# WRONG — double counts overlap:
wrong = P_spam + P_free
print(f"Wrong: {wrong}")   # 0.30

# CORRECT — subtract the overlap once:
correct = P_spam + P_free - P_spam_and_free
print(f"Correct P(spam OR free) = {correct}")  # 0.22
print(f"Correct P(spam AND free) = {P_spam_and_free}")
# The formula: P(A OR B) = P(A) + P(B) - P(A AND B)