def prob(k, m, n):
    total= k+m+n
    prob_mm_aa = (m / total) * ((m - 1) / (total - 1)) * 0.25
    prob_mn_aa = 2 * (m / total) * (n / (total - 1)) * 0.5
    prob_nn_aa = (n / total) * ((n - 1) / (total - 1)) * 1.0

    total_recessive_prob = prob_mm_aa + prob_mn_aa + prob_nn_aa

    dominant_prob= 1.0 - total_recessive_prob

    return dominant_prob
k, m, n= 24, 16, 20
print(f"Result: {prob(k, m, n):.5f}")
