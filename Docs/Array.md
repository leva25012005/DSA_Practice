# Array

## 📑 Mục lục

1. [Introductionu](#Introduction)
2. [Các kỹ thuật cơ bản](#-các-kỹ-thuật-cơ-bản)
3. [Common Array Problem-Solving Techniques](#-Common-Array-Problem-Solving-Techniques)
4. [DList of Solved Problems](#-list-of-Solved-Problems)

---

## 📖 Introduction

### ✏️Concept

- **Array** is **a linear data structure** that stores **elements of the same types** in **contiguous memory locations**, accessed by an index
- Types of Arrays:

  ![alt text](Types-of-Arrays.webp)

### ✅Advantages

- 🚀 Fast Access (O(1)): Direct random access to any element using its index.
- 🧠 Cache Friendly: Elements stored in contiguous memory → better performance due to locality of reference.
- 📚 Foundation for Other Structures: Basis for strings, matrices, heaps, stacks, queues, graphs, hash tables, etc.
- 💾 Memory Efficiency: Stored in one continuous block → less fragmentation.
- 🔧 Versatility & Compatibility: Can hold different data types and works well with most hardware architectures.

### ❌Disadvantages

- ⚠️ Fixed Size (Static Arrays): Cannot grow or shrink after declaration.
- 🛠️ Costly Insert/Delete: Adding or removing elements in the middle requires shifting → O(n) time.
- 🔍 Inefficient Search: Searching in an unsorted array is O(n).
- 📦 Wasted Memory: If the declared size is larger than needed → unused space.
- 🔄 Resizing Overhead (Dynamic Arrays): When capacity is exceeded, resizing takes O(n) time.
- 🎯 Limited Flexibility: Arrays only store elements of the same type and are less adaptable than structures like Linked List, Tree, Hash Table.

---

## 🔑 Common Array Problem-Solving Techniques

| #   | **Technique**                | **Complexity (Time/Space)** | **Example Problems**                         | **Note**                                                                  |
| --- | ---------------------------- | --------------------------- | -------------------------------------------- | ------------------------------------------------------------------------- |
| 1   | 👣 Traversal                 | O(n) / O(1)                 | Find sum, min/max, check conditions          | Basic iteration over the entire array                                     |
| 2   | 🎯 Two Pointers              | O(n) / O(1)                 | Two Sum II, 3Sum, Remove Duplicates          | Use two indices moving inward or parallel to optimize pair/triplet search |
| 3   | ⚡ Prefix Sum                | O(n) / O(n)                 | Subarray Sum, Range Query                    | Precompute cumulative sums for fast range queries                         |
| 4   | 🪟 Sliding Window            | O(n) / O(1)                 | Maximum Subarray, Longest Substring          | Maintain a dynamic window over the array for subarray/substring problems  |
| 5   | 🔢 Counting/Frequency        | O(n) / O(k)                 | Anagram check, Counting Sort                 | Use arrays/maps to count occurrences (effective when range is small)      |
| 6   | 🗂 Hash Map (Hashing)         | O(n) / O(n)                 | Two Sum, Subarray Sum Equals K               | Store index/frequency for quick lookups                                   |
| 7   | 🔀 Sorting-based             | O(n log n)                  | Merge Intervals, Meeting Rooms               | Sort first, then apply greedy, binary search, or two pointers             |
| 8   | 📏 Binary Search             | O(log n) / O(1)             | Search in Rotated Array, Peak Element        | Efficient search in sorted or rotated arrays                              |
| 9   | 📉 Monotonic Stack           | O(n) / O(1)                 | Next Greater Element, Largest Histogram      | Use increasing/decreasing stack for range queries                         |
| 10  | ⛰ Heap (Priority Queue)      | O(n log k)                  | Kth Largest Element, Top K Frequent          | Maintain top-k elements or process streaming data                         |
| 11  | ⚔ Divide & Conquer           | O(n log n)                  | Merge Sort, Max Subarray (D&C)               | Split into subproblems and combine results                                |
| 12  | 🔁 Dynamic Programming       | O(n) / O(n)                 | House Robber, DP on arrays                   | Store intermediate results to avoid recomputation                         |
| 13  | 💡 Greedy + Array            | O(n log n)                  | Interval Scheduling, Minimum Arrows          | Make local optimal decisions, often with sorting/heap                     |
| 14  | 🔄 Cycle Detection (Floyd’s) | O(n) / O(1)                 | Find Duplicate Number, Linked List Cycle     | Detect cycles using fast/slow pointers                                    |
| 15  | 🧩 Matrix-based              | O(n·m) / O(1)               | Rotate Matrix, Spiral Traversal, Word Search | Apply array techniques to 2D grids                                        |
| 16  | 🪅 Partitioning/Grouping     | O(n) / O(1)                 | Dutch National Flag, Group Anagrams          | Rearrange/group elements based on conditions                              |
| 17  | 📈 Kadane’s Algorithm        | O(n) / O(1)                 | Maximum Subarray, Circular Subarray          | DP-like linear scan to find maximum sum subarray                          |

---

## 📂 List of Solved Problems

| ID   | Problem                 | Link                                                                 | Status | Note                |
| ---- | ----------------------- | -------------------------------------------------------------------- | ------ | ------------------- |
| 0001 | Two Sum                 | [LeetCode](https://leetcode.com/problems/two-sum/)                   | ✅     | HashMap             |
| 0053 | Maximum Subarray        | [LeetCode](https://leetcode.com/problems/maximum-subarray/)          | 🚧     | Kadane’s Algorithm  |
| 0121 | Best Time to Buy & Sell | [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell/) | ⏳     | Prefix Sum + Greedy |

👉 Gợi ý: Dùng script automation để update bảng này từ folder `solutions/leetcode/`.

---
