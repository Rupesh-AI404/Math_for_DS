# The formula: P(A|B) = P(B|A) * P(A) / P(B)
# Real example from the book: cancer + coffee study

P_coffee               = 0.65   # 65% of people drink coffee
P_cancer               = 0.005  # 0.5% have cancer
P_coffee_given_cancer  = 0.85   # 85% of cancer patients drink coffee

# Question: P(cancer | drinks coffee) = ?
P_cancer_given_coffee  = (P_coffee_given_cancer * P_cancer) / P_coffee

print(f"P(cancer | coffee) = {P_cancer_given_coffee:.4f}")  # 0.0065
# Only 0.65%! The headline "85% of cancer patients drink coffee"
# sounds scary but flipping the condition reveals it's nearly nothing.
# THIS is why Bayes matters — direction of condition is everything.