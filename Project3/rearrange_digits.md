Given an unsorted array, first I sort the array using merged sort

Time complexity of the merge sort is O(nlogn), splace complexity is O(n) to store all the elements

To get the highest two numbers out of a sorted array, we assign all even index elements into one element, the rest odd index elements into the second number (higher value elements are assigned first)

Example: [1,3,5,6,7,9] -> 963 and 751
