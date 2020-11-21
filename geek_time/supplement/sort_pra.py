# bubble sorting
def bubble_sort(arr):
    length = len(arr)
    for i in range(1, length):
        swapped = False
        for j in range(length-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break


# bubble sort singlelinkedlist
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def bubble_sort_linked_list(head):
    dummy = Node()
    dummy.next = head
    end = None

    while dummy.next.next != end:
        p = dummy
        swapped = False
        while p.next.next != end:
            if p.next.val > p.next.next.val:
                swapped = True
                x, y = p.next, p.next.next
                x.next = y.next
                y.next = x
                p.next = y
            p = p.next

        end = p.next
        if not swapped:
            break
    return dummy.next


# insertion sort
def insertion_sort(arr):
    length = len(arr)
    for i in range(1, length):
        value = arr[i]
        j = i - 1
        while j >= 0:
            if arr[j] > value:
                arr[j+1] = arr[j]
            else:
                break
            j -= 1
        arr[j+1] = value


if __name__ == "__main__":
    arr = [i for i in range(10, -1, -1)]
    insertion_sort(arr)
    print(arr)

    # head = Node(5)
    # head.next = Node(4)
    # head.next.next = Node(2)
    # head.next.next.next = Node(3)
    # head.next.next.next.next = Node(6)
    # new_head = bubble_sort_linked_list(head)
    #
    # p = new_head
    # sorted_list = []
    # while p:
    #     sorted_list.append(p.val)
    #     p = p.next
    #
    # print('=>'.join(map(str, sorted_list)))

    # arr = [i for i in range(10, -1, -1)]
    # print(arr)
    # bubble_sort(arr)
    # print(arr)