function twoSum(nums, target) {
    var myMap = new Map();
    nums.forEach(function (value, index) {
        var complement = target - value;
        if (myMap.has(complement)) {
            return [myMap.get(complement), index];
        }
        myMap.set(value, index);
    });
    return [];
}
var nums = [2, 7, 11, 15], target = 5;
var result = twoSum(nums, target);
console.log(result);
