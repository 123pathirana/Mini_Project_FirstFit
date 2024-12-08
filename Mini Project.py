# Memory partitions and process sizes
memory_partitions = [100, 500, 200, 300, 600]  # List of memory partitions (in KB)
process_sizes = [212, 417, 112, 426]  # List of process sizes (in KB)

# To store allocation status of processes
allocations = [-1] * len(process_sizes)  # Initialize all processes as not allocated (-1)

# Create a copy of memory partitions to track remaining sizes
remaining_partitions = memory_partitions.copy()

# First Fit allocation algorithm
for i, process in enumerate(process_sizes):  # Iterate through each process
    for j in range(len(remaining_partitions)):  # Check all partitions
        # Allocate if the partition is free and large enough to fit the process
        if remaining_partitions[j] >= process and allocations.count(j) == 0:
            allocations[i] = j  # Assign this partition to the current process
            remaining_partitions[j] -= process  # Reduce the size of the partition
            break  # Exit loop after allocation

# Display results
print("Process No.\tProcess Size\tPartition No.\tFragmentation")
for i, process in enumerate(process_sizes):  # Loop through each process
    if allocations[i] != -1:
        # If allocated, calculate and display fragmentation
        allocated_partition = allocations[i]
        fragmentation = memory_partitions[allocated_partition] - remaining_partitions[allocated_partition]
        print(f"P{i+1}\t\t{process} KB\t\t{allocated_partition+1}\t\t{fragmentation} KB")
    else:
        # If not allocated, indicate so
        print(f"P{i+1}\t\t{process} KB\t\tNot Allocated\t-")

# Display remaining memory in partitions after all allocations
print("\nRemaining Memory in Partitions:")
for i, partition in enumerate(remaining_partitions):
    print(f"Partition {i+1}: {partition} KB")
