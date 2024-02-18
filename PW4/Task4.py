class FibonacciContainer:
    def __init__(self, n):
        self.fibonacci_list = self.generate_fibonacci(n)

    def generate_fibonacci(self, n):
        fibonacci_list = [0, 1]
        while len(fibonacci_list) < n:
            next_fib = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_fib)
        return fibonacci_list

    def __len__(self):
        return len(self.fibonacci_list)

    def __getitem__(self, index):
        return self.fibonacci_list[index]

# Створюємо об'єкт класу FibonacciContainer з n = 10
fib_container = FibonacciContainer(10)

# Виводимо довжину контейнера та перші 5 чисел
print("Довжина контейнера:", len(fib_container))
print("Перші 5 чисел:", fib_container[:5])

