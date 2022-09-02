import pandas as pd

df = pd.read_csv('tiktok/TikTok_songs_2019.csv', delimiter=',')
arr=df['danceability'].to_numpy()
n = len(arr)

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2 
    
    if left < n and arr[largest] < arr[left]:
        largest = left
 
    if right < n and arr[largest] < arr[right]:
        largest = right
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
 
        heapify(arr, n, largest)
 
 
def heapSort(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0)

heapSort(arr, n)

for i in range(n):
    print(arr[i])
