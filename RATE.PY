T = int(input())

# Iterate through each test case
for _ in range(T):
    # Read the rank of Chef
    X = int(input())
    
    # Check if Chef made it to the top 10
    if X <= 10:
        print("YES")
    else:
        print("NO")
