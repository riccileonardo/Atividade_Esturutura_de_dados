# -------------------------------------------------------------------------------------------------------------------
# 3.Crie e preencha (com o método do exercício1) um vetor com 1000 posições e ordene-o utilizando o método de Inserção.
# -------------------------------------------------------------------------------------------------------------------
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def fill_array(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(1, 100)
arr = [0] * 10

fill_array(arr)
print("Vetor preenchido:", arr)
insertion_sort(arr)