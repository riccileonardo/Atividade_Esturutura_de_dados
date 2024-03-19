# -------------------------------------------------------------------------------------------------------------------
# 2. Crie e preencha (com o método do exercício1) um vetor com 1000 posições e ordene-o utilizando o método Buble Sort.
# -------------------------------------------------------------------------------------------------------------------

import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

array = [random.randint(1, 100) for _ in range(10)]
print("Vetor preenchido:", array)

bubble_sort(array)