def tower_of_hanoi(n, source, target, auxiliary):
    if n==1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, target, source)
def tower_of_hanoi_solver(num_disks):
    print(f"Solving Tower of Hanoi problem for {num_disks} disks:")
    tower_of_hanoi(num_disks, 'A','C','B')
if __name__=="__main__":
    num_disks=3
    tower_of_hanoi_solver(num_disks)