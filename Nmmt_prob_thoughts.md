**There are three possibilities:**

1. `N - 1 < 5 - S`:  
The player cannot be Nmmted.

2. `N - 1 = 5 - S`:  
My initial formula works.

3. `N - 1 < 5 - S`:  
We need a new formula for this.
    - The player could land on the 6th play, or above it.
    - The probability EQUALS the probability of (5 - S) players playing within the range AND NOT (N - [5 - S]) players playing within the range.
    - P = [D/A * (D-1)/(A-1) * (D-2)/(A-2)] AND NOT [(D-3)/(A-3) OR (D-3)/(A-3) OR (D-3)/(A-3)]  
    3 players needed to Nmmt you, 3 that could take the Nmmt instead.