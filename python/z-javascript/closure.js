function retirement(retirementAge) {
	var a = ' year left until retirement.';

	return function (yearOfBirth) {
		var age = 2020 - yearOfBirth;
		console.log(retirementAge - age + a);
	};
}

var retirementUS = retirement(66);
var retirementGermany = retirement(65);
var retirementVietnam = retirement(60);

retirementUS(1992);
retirementGermany(1992);
retirementVietnam(1992);
// retirement(66)(1992);

/*
 *	We started by calling retirement() function as passed the value of 66, right?
 *	Then retirement() function then declares this "a" variable here return anonymous function.
 *	Then the function finishes, and its execution context get popped off the stack.
 * 	So after the function returns, now the execution context of the retirement() function is effectively gone,
 *  and with it, the variable object and the entire scope chain should be gone, right??? => ACTUALLY, NO.
 *  The secret of closure is, that even after a function returns, and execution context is gone, THE VARIABLE OBJECT IS STILL THERE. IT'S NOT GONE.
 *	It still sits here in memory and it can be accessed, and that's why we still it there in the execution stack on the left side,
 * 	and also in the scope chain on the right side, because the scope chain is in fact a pointer to variable objects, and in this case, the variable object
 *  that we have here on the stack.
 */

/*
 * Closures Summary
 * An inner function has always access to the variables and parameters of its outer function, even after the function has returned.
 *
 */

/*
 *	Interview questions related to Closures
 *	https://brackets.clementng.me/post/24150213014/example-of-a-javascript-closure-settimeout-inside
 *
 */

// Before:
// (function exe() {
// 	for (var i = 1; i <= 5; i++) {
// 		setTimeout(function () {
// 			console.log(i);
// 		}, 1000 * i); // 6 6 6 6 6
// 	}
// })();

(function exe() {
	for (var i = 1; i <= 5; i++) {
		setTimeout(
			(() => {
				return function (x) {
					console.log(x);
				};
			})(i),
			1000 * i
		); // 6 6 6 6 6
	}
})();

function afterTwoSeconds(value) {
	return new Promise((resolve) => {
		setTimeout(() => {
			resolve(value);
		}, 2000);
	});
}
