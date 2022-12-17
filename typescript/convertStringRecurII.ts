function convertString(input) {
  // Initialize an empty result object
  const result = { and: [] };

  // Split the input string on " AND "
  const clauses = input.split(" AND ");

  // Iterate through the clauses
  for (const clause of clauses) {
    // If the clause starts with "{" and ends with "}", it's a number
    if (clause.startsWith("{") && clause.endsWith("}")) {
      // Extract the number from the clause and add it to the result object
      result.and.push(parseInt(clause.slice(1, -1)));
    } else {
      // The clause must be an AND or OR clause, so split it on " OR "
      const items = clause.split(" OR ");

      // Initialize an OR object with an empty "or" array
      const orObject = { or: [] };

      // Iterate through the items in the OR clause
      for (const item of items) {
        // If the item starts with "{" and ends with "}", it's a number
        if (item.startsWith("{") && item.endsWith("}")) {
          // Extract the number from the item and add it to the OR object
          orObject.or.push(parseInt(item.slice(1, -1)));
        } else {
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
const input = '{1069} AND ({1070} OR {1071} OR {1072}) AND {1244} AND ({1245} OR {1339})';
const output = convertString(input);
console.log(output);