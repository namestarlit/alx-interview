## 0x08. Making Change
### Coin Change Problem

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given total amount.

### Prototype

```python
def makeChange(coins, total)
```

### Return

The function should return the fewest number of coins needed to meet the total amount.

- If the total is 0 or less, return 0.
- If the total cannot be met by any combination of coins you have, return -1.

### Parameters

- `coins`: A list of the values of the coins in your possession.
- `total`: The target total amount to be achieved.

### Constraints

- The value of a coin will always be an integer greater than 0.
- You can assume you have an infinite number of each denomination of coin in the list.
