# Independence test: P(A AND B) should equal P(A) * P(B) if independent
P_spam    = 0.20
P_free    = 0.10
P_both    = 0.08   # what we actually observe

expected_if_independent = P_spam * P_free   # 0.02
print(f"Expected if independent: {expected_if_independent}")
print(f"Actual joint:            {P_both}")
print(f"Dependent? {P_both != expected_if_independent}")  # True → they ARE dependent

# Naive Bayes ignores this and assumes independence anyway:
# P(spam | word1, word2, word3) ≈ P(spam) * P(w1|spam) * P(w2|spam) * P(w3|spam)
# Wrong assumption — yet works well in practice for text classification