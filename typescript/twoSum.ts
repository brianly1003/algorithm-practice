function twoSum(nums: number[], target: number) {
    let myMap = new Map();

    nums.forEach((value, index) => {
        let complement = target - value;

        if (myMap.has(complement)) {
            return [myMap.get(complement), index];
        }

        myMap.set(value, index);
    });

    return [];
}

const nums = [2, 7, 11, 15], target = 5;
const result = twoSum(nums, target);

console.log(result);

