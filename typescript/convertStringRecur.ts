function convertStringRecur(input) {
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
      // The clause must be an AND or OR clause, so call convertString recursively
      result.and.push(convertStringRecur(clause));
    }
  }

  return result;
}

const input = '{1069} AND ({1070} OR {1071} OR {1072}) AND {1244} AND ({1245} OR {1339})';
const output = convertStringRecur(input);
console.log(output);
