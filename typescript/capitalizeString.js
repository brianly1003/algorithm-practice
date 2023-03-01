/*
!    Write a function that accepts a String as an argument

!    The function should capitalize ONLY every other letter in the String

!    The function should then return the converted String.
*/

// TODO: Brute Force    [O(N) & O(N)]

function capitalizeString(str) {
  let dict = {};
  let result = [];

  for (let i = 0; i < str.length; i++) {
    if (typeof dict[str[i]] === "undefined") {
      result.push(str[i].toUpperCase());
      dict[str[i]] = 1;
    } else {
      result.push(str[i]);
    }
  }
  return result.join("");
}

function capitalizeString(str) {
  return Array.from(str).reduce((accumulator, currentValue, currentIndex) => {
    if (currentIndex === 1) accumulator = accumulator.toUpperCase();

    if (accumulator && accumulator.includes(currentValue.toUpperCase())) {
      accumulator += currentValue;
    } else {
      accumulator += currentValue.toUpperCase();
    }

    return accumulator;
  });
}

const input = "abccadeef";
const result = capitalizeString(input);
console.log(`Result is ${result}`);
