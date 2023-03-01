// TODO: Sliding Window   [O(N) & O(1)]

function maxSumSubArray(arr, size) {
  // Edge case: Array is too small
  if (arr.length < size) return null;

  let maxSum = 0;

  let windowSum = arr.slice(0, size).reduce((a, b) => a + b);
  maxSum = Math.max(maxSum, windowSum);

  for (let i = size; i < arr.length; i++) {
    windowSum -= arr[i - size];

    windowSum += arr[i];

    maxSum = Math.max(maxSum, windowSum);
  }

  return maxSum;
}

const arr = [1, 2, 3, 4, 5, 6];
const size = 2;
const result = maxSumSubArray(arr, size);
console.log(`Sum is ${result}`);

// Canva
// Unsplash
// Pexels
// Genially

