# Array

## 📑 Table of Contents

1. [Introductionu](#Introduction)
2. [Common Array Problem-Solving Techniques](#-Common-Array-Problem-Solving-Techniques)
3. [List of Solved Problems](#-list-of-Solved-Problems)
4. [Common Array Problem-Solving Techniques — C++ Template Code](#-common-array-problem-solving-techniques)

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

| #   | **Technique**                                              | **Complexity (Time/Space)** | **Example Problems**                         | **Note**                                                                  |
| --- | ---------------------------------------------------------- | --------------------------- | -------------------------------------------- | ------------------------------------------------------------------------- |
| 1   | 👣 [Traversal](#1-traversal)                               | O(n) / O(1)                 | Find sum, min/max, check conditions          | Basic iteration over the entire array                                     |
| 2   | 🎯 [Two Pointers](#2-two-pointers)                         | O(n) / O(1)                 | Two Sum II, 3Sum, Remove Duplicates          | Use two indices moving inward or parallel to optimize pair/triplet search |
| 3   | ⚡ [Prefix Sum](#3-prefix-sum)                             | O(n) / O(n)                 | Subarray Sum, Range Query                    | Precompute cumulative sums for fast range queries                         |
| 4   | 🪟 [Sliding Window](#4-sliding-window)                     | O(n) / O(1)                 | Maximum Subarray, Longest Substring          | Maintain a dynamic window over the array for subarray/substring problems  |
| 5   | 🔢 [Counting/Frequency](#5-countingfrequency)              | O(n) / O(k)                 | Anagram check, Counting Sort                 | Use arrays/maps to count occurrences (effective when range is small)      |
| 6   | 🗂 [Hash Map (Hashing)](#6-hash-map-hashing)                | O(n) / O(n)                 | Two Sum, Subarray Sum Equals K               | Store index/frequency for quick lookups                                   |
| 7   | 🔀 [Sorting-based](#7-sorting-based)                       | O(n log n)                  | Merge Intervals, Meeting Rooms               | Sort first, then apply greedy, binary search, or two pointers             |
| 8   | 📏 [Binary Search](#8-binary-search)                       | O(log n) / O(1)             | Search in Rotated Array, Peak Element        | Efficient search in sorted or rotated arrays                              |
| 9   | 📉 [Monotonic Stack](#9-monotonic-stack)                   | O(n) / O(1)                 | Next Greater Element, Largest Histogram      | Use increasing/decreasing stack for range queries                         |
| 10  | ⛰ [Heap (Priority Queue)](#10-heap-priority-queue)         | O(n log k)                  | Kth Largest Element, Top K Frequent          | Maintain top-k elements or process streaming data                         |
| 11  | ⚔ [Divide & Conquer](#11-divide--conquer)                  | O(n log n)                  | Merge Sort, Max Subarray (D&C)               | Split into subproblems and combine results                                |
| 12  | 🔁 [Dynamic Programming](#12-dynamic-programming)          | O(n) / O(n)                 | House Robber, DP on arrays                   | Store intermediate results to avoid recomputation                         |
| 13  | 💡 [Greedy + Array](#13-greedy--array)                     | O(n log n)                  | Interval Scheduling, Minimum Arrows          | Make local optimal decisions, often with sorting/heap                     |
| 14  | 🔄 [Cycle Detection (Floyd’s)](#14-cycle-detection-floyds) | O(n) / O(1)                 | Find Duplicate Number, Linked List Cycle     | Detect cycles using fast/slow pointers                                    |
| 15  | 🧩 [Matrix-based](#15-matrix-based-2d-array)               | O(n·m) / O(1)               | Rotate Matrix, Spiral Traversal, Word Search | Apply array techniques to 2D grids                                        |
| 16  | 🪅 [Partitioning/Grouping](#16-partitioninggrouping)       | O(n) / O(1)                 | Dutch National Flag, Group Anagrams          | Rearrange/group elements based on conditions                              |
| 17  | 📈 [Kadane’s Algorithm](#17-kadanes-algorithm)             | O(n) / O(1)                 | Maximum Subarray, Circular Subarray          | DP-like linear scan to find maximum sum subarray                          |

---

## 🔑 Common Array Problem-Solving Techniques — C++ Template Code

### 1. Traversal

```cpp
// Traverse and process all elements
for (int i = 0; i < n; ++i) {
    // process arr[i]
}
```

### 2. Two Pointers

```cpp
// Example: Remove duplicates from sorted array
int i = 0, j = 0;
while (j < n) {
    if (arr[j] != arr[i]) arr[++i] = arr[j];
    ++j;
}
// arr[0..i] is unique
```

### 3. Prefix Sum

```cpp
// Build prefix sum
vector<int> prefix(n+1, 0);
for (int i = 0; i < n; ++i)
    prefix[i+1] = prefix[i] + arr[i];
// Range sum arr[l..r]: prefix[r+1] - prefix[l]
```

### 4. Sliding Window

```cpp
// Example: Longest subarray with sum <= k
int l = 0, sum = 0, ans = 0;
for (int r = 0; r < n; ++r) {
    sum += arr[r];
    while (sum > k) sum -= arr[l++];
    ans = max(ans, r - l + 1);
}
```

### 5. Counting/Frequency

```cpp
// Counting frequency (value range known: 0..maxVal)
vector<int> freq(maxVal+1, 0);
for (int x : arr) freq[x]++;
```

### 6. Hash Map (Hashing)

```cpp
unordered_map<int, int> mp;
// Example: Two Sum
for (int i = 0; i < n; ++i) {
    int need = target - arr[i];
    if (mp.count(need)) {
        // found pair (mp[need], i)
    }
    mp[arr[i]] = i;
}
```

### 7. Sorting-based

```cpp
// Standard sort
sort(arr.begin(), arr.end());
```

### 8. Binary Search

```cpp
int l = 0, r = n-1;
while (l <= r) {
    int m = l + (r-l)/2;
    if (arr[m] == target) {/*found*/}
    else if (arr[m] < target) l = m+1;
    else r = m-1;
}
```

### 9. Monotonic Stack

```cpp
// Next Greater Element
stack<int> st;
vector<int> res(n, -1);
for (int i = 0; i < n; ++i) {
    while (!st.empty() && arr[i] > arr[st.top()]) {
        res[st.top()] = arr[i];
        st.pop();
    }
    st.push(i);
}
```

### 10. Heap (Priority Queue)

```cpp
// Kth largest element
priority_queue<int, vector<int>, greater<int>> pq;
for (int x : arr) {
    pq.push(x);
    if (pq.size() > k) pq.pop();
}
int ans = pq.top();
```

### 11. Divide & Conquer

```cpp
// Merge Sort skeleton
void mergeSort(vector<int>& a, int l, int r) {
    if (l >= r) return;
    int m = (l + r) / 2;
    mergeSort(a, l, m);
    mergeSort(a, m+1, r);
    // merge a[l..m] and a[m+1..r]
}
```

### 12. Dynamic Programming

```cpp
// Example: House Robber
vector<int> dp(n+1, 0);
dp[0]=0; dp[1]=arr[0];
for (int i=2; i<=n; ++i)
    dp[i]=max(dp[i-1], dp[i-2]+arr[i-1]);
```

### 13. Greedy + Array

```cpp
// Jump Game: Can reach end?
int far = 0;
for (int i=0; i<n; ++i) {
    if (i > far) return false;
    far = max(far, i + arr[i]);
}
return true;
```

### 14. ycle Detection (Floyd’s)

```cpp
int slow = arr[0], fast = arr[0];
do {
    slow = arr[slow];
    fast = arr[arr[fast]];
} while (slow != fast);
// Now find entry point if needed
```

### 15. Matrix-based (2D Array)

```cpp
// Spiral order traversal of matrix
vector<int> spiralOrder(vector<vector<int>>& mat) {
    vector<int> res;
    int m = mat.size(), n = mat[0].size();
    int top=0, bot=m-1, left=0, right=n-1;
    while (top<=bot && left<=right) {
        for (int j=left; j<=right; ++j) res.push_back(mat[top][j]);
        ++top;
        for (int i=top; i<=bot; ++i) res.push_back(mat[i][right]);
        --right;
        if (top<=bot)
            for (int j=right; j>=left; --j) res.push_back(mat[bot][j]);
        --bot;
        if (left<=right)
            for (int i=bot; i>=top; --i) res.push_back(mat[i][left]);
        ++left;
    }
    return res;
}
```

### 16. Partitioning/Grouping

```cpp
// Dutch National Flag (0,1,2 sorting)
int l=0, m=0, r=n-1;
while (m <= r) {
    if (arr[m] == 0) swap(arr[l++], arr[m++]);
    else if (arr[m] == 1) ++m;
    else swap(arr[m], arr[r--]);
}
```

### 17. Kadane’s Algorithm

```cpp
int maxSum = arr[0], cur = arr[0];
for (int i=1; i<n; ++i) {
    cur = max(arr[i], cur + arr[i]);
    maxSum = max(maxSum, cur);
}
```

## 📂 List of Solved Problems

### 📘 LeetCode Problems

**Progress:** 0 / 200 (0%)

`[--------------------]`

| ID | Problem | Link | Status | Note |

### 🟢 GeeksforGeeks Problems

**Progress:** 0 / 200 (0%)

`[--------------------]`

| ID | Problem | Link | Status | Note |
