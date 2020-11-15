import random
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import timeit
import time
import pdb

Arr = np.random.randint(0,100,100)
print(Arr)

# Sorting algos
def selection_sort(Arr):
	for min in range(len(Arr)):
		
		loc = np.argmin(Arr[min:])
		loc = loc + min

		Arr = swap(Arr, min, loc)
		yield Arr
def bubble_sort(Arr):
	
	
	finished = False
	while finished == False:

		# check if done by iteration through the list with no swaps
		consecutive = 0
		
		for i in range(len(Arr) - 1):
			j = i + 1

			if Arr[i] > Arr[j]:
				swap(Arr, i, j)
				consecutive += 1


			yield Arr
		
		# check if done		
		if consecutive == 0:
			finished = True
	yield Arr		

def quick_sort(Arr,bot,top):
	
	pivot = Arr[top]
	i = bot
	if bot < top:
		for k in range(bot,top):
			if Arr[k] < pivot:
				swap(Arr, i, k)
				i += 1
				yield Arr	
		swap(Arr,i,top)
	
		yield Arr	
		yield from quick_sort2(Arr,bot,i - 1)
		yield from quick_sort2(Arr,i + 1,top)



# Swap - swaps two elements from the input array in place
def swap(A,i,j):
	if A[i] == A[j]:
		return A

	ph = A[i]
	A[i] = A[j]
	A[j] = ph
	return A

algo = quick_sort(Arr,0,len(Arr) -1)
#algo = bubble_sort(Arr)
titles = ["Bubble Sort","Selection Sort","quick_sort"]

# makes the figure and the graph
fig, ax = plt.subplots()
ax.set_title(titles[2])
bar_rec = ax.bar(range(len(Arr)), Arr, align='edge')
text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

epochs = [0]
def update_plot(Arr, rec, epochs):

    for rec, val in zip(rec, Arr):
        rec.set_height(val)
    epochs[0]+= 1
    text.set_text("No.of operations :{}".format(epochs[0]))

anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec, epochs), frames=algo, interval=1, repeat=False)
plt.show()








