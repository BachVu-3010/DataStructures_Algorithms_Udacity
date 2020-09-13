For this problem I used the two pointers method, one is a low and the other is a high pointer. As I traverse the array, all numbers 0 are moved before low pointer, all numbers 2 are moved after high pointer. Between low - high pointer is number 1.

[0,0, .. low , 1, 1, 1, high , 2, 2, 2]

Time complexity 0(n) as I traversed the array only once

Space complextiy 0(1) as I only modified the initial array
