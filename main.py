import tkinter as tk

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display_list(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " "
            current = current.next
        return result

    def sort_list(self):
        # Власний алгоритм сортування (можна використовувати більш ефективні алгоритми)
        nodes = []
        current = self.head
        while current:
            nodes.append(current.data)
            current = current.next
        nodes.sort()
        self.head = None
        for value in nodes:
            self.add_node(value)

class LinkedListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Linked List App")

        # Задання фіксованих розмірів вікна
        self.root.geometry("500x300")

        self.linked_list = LinkedList()

        self.label = tk.Label(root, text="Enter value:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.add_button = tk.Button(root, text="Add Node", command=self.add_node)
        self.add_button.pack()

        self.display_button = tk.Button(root, text="Display List", command=self.display_list)
        self.display_button.pack()

        self.sort_button = tk.Button(root, text="Sort List", command=self.sort_list)
        self.sort_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def add_node(self):
        value = self.entry.get()
        if value.isdigit():
            self.linked_list.add_node(int(value))
            self.result_label.config(text=f"List: {self.linked_list.display_list()}")
        else:
            self.result_label.config(text="Please enter a valid integer.")

    def display_list(self):
        self.result_label.config(text=f"List: {self.linked_list.display_list()}")

    def sort_list(self):
        self.linked_list.sort_list()
        self.result_label.config(text=f"Sorted List: {self.linked_list.display_list()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = LinkedListApp(root)
    root.mainloop()
