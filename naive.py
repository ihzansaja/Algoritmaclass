import random
from collections import Counter


random.seed(40)

data = [random.randint(0, 100) for _ in range(50)]
print("Data Acak:", data)

def naive_bayes_sort(arr):
    # Hitung frekuensi setiap elemen
    freq = Counter(arr)
    
    sorted_arr = []
    for key in sorted(freq.keys()):
        sorted_arr.extend([key] * freq[key])
    return sorted_arr

sorted_naive_bayes = naive_bayes_sort(data)
print("Hasil Sorting dengan Naive Bayes:", sorted_naive_bayes)

