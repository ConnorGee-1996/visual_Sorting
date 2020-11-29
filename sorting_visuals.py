import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
import random

# Arr = np.random.randint(0,100,50)
# Arr = np.array([6, 41, 41, 50, 51, 59, 78, 41, 52, 24])
# Arr = np.arange(50)
Arr = []
for i in range(0, 50):
    n = random.randint(1, 30)
    Arr.append(n)
print(Arr)

# Sorting algorithms - adding different colors
def selection_sort(arr):
    num_op = 0
    num_swaps = 0
    i = 0
    k = 0
    sorted_ids = []
    while i < len(Arr) - 1:
        smallest = i
        num_op += 1
        for k in range(i, len(arr)):

            if arr[smallest] > arr[k]:
                smallest = k
            num_op += 1

            # output the array with k, to show the index's being compared
            yield arr, num_op, sorted_ids, num_swaps, k, smallest
        swap(arr, i, smallest)

        # every swap add to the number of swaps and add the index for the sorted array to sorted.
        num_swaps += 1
        sorted_ids.append(i)

        yield arr, num_op, sorted_ids, num_swaps, k, i  # Arr  np.append(Arr, num_op),sorted_ids
        i += 1

    sorted_ids.append(i)
    yield arr, num_op, sorted_ids, num_swaps, k, i  # Arr


def bubble_sort(arr):
    i = 0
    j = 0
    num_op = [0]
    num_swaps = 0

    sorted_id = []
    counter = 0

    while True:
        # check if done by iteration through the list with no swaps
        consecutive = 0

        for i in range(len(arr) - counter - 1):
            j = i + 1

            if arr[i] > arr[j]:
                swap(arr, i, j)
                consecutive += 1
                num_swaps += 1

            num_op[0] += 1
            yield arr, num_op, sorted_id, num_swaps, i, j  # Arr

        sorted_id.append(len(arr) - counter)
        counter += 1

        # check if done
        num_op[0] += 1
        if len(sorted_id) == len(arr):
            break

    sorted_id.append(i)
    yield arr, num_op, sorted_id, num_swaps, i, j  # Arr


def quick_sort_end(arr, bot, top, sorted_ids):
    num_ops = 0
    num_swaps = 0
    sorted_ids = sorted_ids

    pivot = arr[top]
    i = bot
    k = 0
    num_ops += 1

    if bot == top:
        sorted_ids.append(i)
        yield arr, num_ops, sorted_ids, num_swaps, bot, top
        num_swaps = 0
        num_ops = 0
    if bot < top:

        for k in range(bot, top):
            num_ops += 1
            if arr[k] < pivot:
                swap(arr, i, k)
                num_swaps += 1

                i += 1
            yield arr, num_ops, sorted_ids, num_swaps, k, i  # np.append(Arr, num_ops) # Arr
            num_swaps = 0
            num_ops = 0
        swap(arr, i, top)
        num_swaps += 1

        sorted_ids.append(i)

        yield arr, num_ops, sorted_ids, num_swaps, k, i  # Arr

        yield from quick_sort_end(arr, bot, i - 1, sorted_ids)
        yield from quick_sort_end(arr, i + 1, top, sorted_ids)


def quick_sort_mid(arr, bot, top, sorted_ids):
    num_op = 0
    num_swaps = 0
    sorted_ids = sorted_ids

    i = bot
    k = top

    mid_point = find_middle(arr[bot:top + 1]) + i

    # if i < k:
    # 	mid_point = medianOfThree(Arr[bot :top+1]) + i
    # else:
    # 	mid_point = 0

    piv_index = mid_point

    num_op += 1
    if piv_index >= len(arr):
        return arr
    pivot = arr[piv_index]

    if bot == top:
        sorted_ids.append(i)
        yield arr, num_op, sorted_ids, num_swaps, bot, top
        num_swaps = 0
        num_op = 0

    num_op += 1
    if i < k:
        while True:

            while arr[i] < pivot:
                num_op += 1
                i += 1
                yield arr, num_op, sorted_ids, num_swaps, k, i
                num_swaps = 0
                num_op = 0
            num_op += 1

            while arr[k] > pivot:
                num_op += 1
                k -= 1
                yield arr, num_op, sorted_ids, num_swaps, k, i
                num_swaps = 0
                num_op = 0
            num_op += 1

            num_op += 1
            if i >= k:
                break

            num_op += 1
            if Arr[i] == Arr[k] == pivot:
                i += 1
                yield arr, num_op, sorted_ids, num_swaps, k, i  # Arr
                num_swaps = 0
                num_op = 0

            num_op += 1
            if Arr[i] != Arr[k]:
                swap(arr, i, k)
                num_swaps += 1

                yield arr, num_op, sorted_ids, num_swaps, k, i  # Arr
                num_swaps = 0
                num_op = 0

        if arr[k] == pivot:
            sorted_ids.append(k)
        elif arr[i] == pivot:
            sorted_ids.append(i)

        yield from quick_sort_mid(arr, bot, k - 1, sorted_ids)
        yield from quick_sort_mid(arr, k + 1, top, sorted_ids)


# def merge_sort(arr, bot, top):
#   return


def find_middle(input_list):
    middle = float(len(input_list)) / 2
    if middle % 2 != 0:
        return int(middle - 0.5)
    else:
        return int(middle)


def median_of_three(arr):
    bot = 0
    top = len(arr) - 1
    middle = round((bot + top / 2))

    a = np.asarray(arr)
    if a.size == 0:
        return 0

    if arr[bot] <= arr[top]:
        if arr[bot] >= arr[middle]:
            return bot
        else:
            if arr[top] >= arr[middle]:
                return middle
            else:
                return top
    else:
        if arr[top] >= arr[middle]:
            return top
        else:
            if arr[bot] >= arr[middle]:
                return middle
            else:
                return bot


# Swap - swaps two elements from the input array in place
def swap(a, i, j):
    if a[i] == a[j]:
        return a

    ph = a[i]
    a[i] = a[j]
    a[j] = ph
    return a


# Set up figure and axes
fig, ax = plt.subplots(figsize=[10, 6])
titles = ["Bubble Sort", "Selection Sort", "quick_sort"]
ax.set_title(titles[1])
bar_rec = ax.bar(range(len(Arr)), Arr, align='edge', color="red")
text = ax.text(0.01, 0.93, "", transform=ax.transAxes)

# recursion algorithms

# #algo = quick_sort_mid(Arr, 0, len(Arr) - 1, [])
# #algo = quick_sort_end(Arr,0,len(Arr) -1,[])
#
# swaps = []
# comp = []
#
#
# def update_plot2(arr, rec, swap_number, comp_number):
#     counter = 0
#
#     if arr[3] != 0:
#         swap_number.append(arr[3])
#     if arr[1] != 0:
#         comp_number.append(arr[1])
#
#     for rec, val in zip(rec, arr[0]):
#         rec.set_height(val)
#
#         # make all unsorted red apart from comparison index
#         if counter == arr[4] or counter == arr[5]:
#             rec.set_color("darkblue")
#         else:
#             rec.set_color("firebrick")
#
#         if counter in arr[2]:
#             rec.set_color("forestgreen")
#
#         if counter == len(arr[0]):
#             rec.set_color("forestgreen")
#
#         counter += 1
#     text.set_text("No.of swaps :{}\nNo.of comparisons: {}".format(sum(swap_number), sum(comp_number)))
#
#
# anima = anim.FuncAnimation(fig, func=update_plot2, fargs=(bar_rec, swaps, comp), frames=algo, interval=1, repeat=False)
# plt.show()

# non recursion algorithms
#algo = selection_sort(Arr)
algo = bubble_sort(Arr)

why = "This has to be inserted into the function else it takes in the array as separate arguments into the function instead of one. not sure why"


def update_plot(Arr, rec,why):
    counter = 0
    for rec, val in zip(rec, Arr[0]):
        rec.set_height(val)

        # make all unsorted red apart from comparison index
        if counter == Arr[4] or counter == Arr[5]:
            rec.set_color("darkblue")
        else:
            rec.set_color("firebrick")

        if counter in Arr[2] :
            rec.set_color("forestgreen")

        if counter == len(Arr[0]):
            rec.set_color("forestgreen")


        counter += 1
    text.set_text("No.of swaps :{}\nNo.of comparisons: {}".format(Arr[3],Arr[1]))


# noinspection PyTypeChecker
anima = anim.FuncAnimation(fig, func=update_plot, fargs=(bar_rec,why), frames =algo, interval=1, repeat=False)
plt.show()
