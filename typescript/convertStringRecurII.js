function convertString(input) {
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
            // The clause must be an AND or OR clause, so split it on " OR "
            var items = clause.split(" OR ");
            // Initialize an OR object with an empty "or" array
            var orObject = { or: [] };
            // Iterate through the items in the OR clause
            for (var _a = 0, items_1 = items; _a < items_1.length; _a++) {
                var item = items_1[_a];
                // If the item starts with "{" and ends with "}", it's a number
                if (item.startsWith("{") && item.endsWith("}")) {
                    // Extract the number from the item and add it to the OR object
                    orObject.or.push(parseInt(item.slice(1, -1)));
                }
                else {
                    // The item must be an AND clause, so call convertString recursively
                    orObject.or.push(convertString(item));
                }
            }
            // Add the OR object to the result object
            result.and.push(orObject);
        }
    }
    return result;
}
// convertStringRecurII.ts
var input = '{1069} AND ({1070} OR {1071} OR {1072}) AND {1244} AND ({1245} OR {1339})';
var output = convertString(input);
console.log(output);
