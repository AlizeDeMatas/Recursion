
def TowerOfHanoi(n, start, dist, temp):
    if n == 1:
        print(f"Move disk 1 from {start} to {dist}")
        return

    TowerOfHanoi(n - 1, start, temp, dist)
    print(f"Move disk {n} from {start} to {dist}")
    TowerOfHanoi(n - 1, temp, dist, start)


TowerOfHanoi(5, "1", "3", "2")

# Driver Code
n = 3
start = 1
dist = 3
temp = 2

