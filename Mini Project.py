# Memory partitions and process sizes
memory_partitions = [100, 500, 200, 300, 600]  # in KB
process_sizes = [212, 417, 112, 426]  # in KB

# To store allocation status of processes and memory partitions
allocations = [-1] * len(process_sizes)  # -1 indicates not allocated
fragmentation = [0] * len(memory_partitions)  # To track fragmentation in each block

# First Fit allocation algorithm
for i, process in enumerate(process_sizes):
    for j, partition in enumerate(memory_partitions):
        # Check if partition can accommodate the process
        if partition >= process:
            allocations[i] = j  # Allocate the partition to the process
            fragmentation[j] = partition - process  # Calculate fragmentation
            memory_partitions[j] -= process  # Reduce the available memory in the partition
            break  # Move to the next process once allocated

# Display results
print("Process No.\tProcess Size\tPartition No.\tFragmentation")
for i, process in enumerate(process_sizes):
    if allocations[i] != -1:
        print(
            f"P{i+1}\t\t{process} KB\t\t{allocations[i]+1}\t\t{fragmentation[allocations[i]]} KB"
        )
    else:
        print(f"P{i+1}\t\t{process} KB\t\tNot Allocated\t-")

# Display unused memory in partitions after allocation
# Fragmentation
print("\nRemaining Memory in Partitions:")
for i, partition in enumerate(memory_partitions):
    print(f"Partition {i+1}: {partition} KB")
