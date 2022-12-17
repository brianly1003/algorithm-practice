function convertStringRecur(input) {
    // Initialize an empty result object
    var result = { and: [] };
    // Split the input string on " AND "
    var clauses = input.split(" AND ");
    // Iterate through the clauses
    for (var _i = 0, clauses_1 = clauses; _i < clauses_1.length; _i++) {
        var clause = clauses_1[_i];
        // If the clause starts with "{" and ends with "}", it's a number
        if (clause.startsWith("{") && clause.endsWith("}")) {
            // Extract the number from the clause and add it to the result object
            result.and.push(parseInt(clause.slice(1, -1)));
        }
        else {
            // The clause must be an AND or OR clause, so call convertString recursively
            result.and.push(convertStringRecur(clause));
        }
    }
    return result;
}
var input = '{1069} AND ({1070} OR {1071} OR {1072}) AND {1244} AND ({1245} OR {1339})';
var output = convertStringRecur(input);
console.log(output);
