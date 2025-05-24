# CSC507 Operating Systems Module 4 Cirtical Thinking
# Simulate the First-Fit Algorithm in Allocating Memory to Processes

# Function to allocate memory to processes using first fit algorithm
def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n 

    # pick each process and find suitable blocks
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i] = j  
                blockSize[j] -= processSize[i] 
                break

    print(f"{'Process No.':<12}{'Process Size':<15}{'Block No.'}")
    print("-" * 40)
    for i in range(n):
        block_no = allocation[i] + 1 if allocation[i] != -1 else "Not Allocated"
        print(f"{i+1:<12}{processSize[i]:<15}{block_no}")


if __name__ == '__main__': 
    blockSize = [100, 500, 250, 325, 600] 
    processSize = [125, 417, 250, 575, 500] #212, 417, 112, 426
    
    # Number of blocks
    m = len(blockSize)
    # Number of processes
    n = len(processSize)

    firstFit(blockSize, m, processSize, n)
    
