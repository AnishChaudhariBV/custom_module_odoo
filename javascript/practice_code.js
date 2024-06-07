//#for loop
1.]
for (let i = 0; i < 5; i++) {
  console.log(i);  // Output: 0, 1, 2, 3, 4
}
2.]
const obj = {a: 1, b: 2, c: 3};
for (let key in obj) {
  console.log(key + ": " + obj[key]);  // Output: a: 1, b: 2, c: 3
}
3.]
const arr = [10, 20, 30];
for (let value of arr) {
  console.log(value);  // Output: 10, 20, 30
}

//#while loop
1.]
let i = 0;
while (i < 5) {
  console.log(i);  // Output: 0, 1, 2, 3, 4
  i++;
}
2.]
let sum = 0;
let num = 1;
while (num <= 100) {
  sum += num;
  num++;
}
console.log("Sum of first 100 natural numbers is:", sum);
// Output: Sum of first 100 natural numbers is: 5050

3.]
let n = 5; // You can change this value to calculate factorial of another number
let factorial = 1;
let i = n;
while (i > 0) {
  factorial *= i;
  i--;
}
console.log(`Factorial of ${n} is:`, factorial);
// Output: Factorial of 5 is: 120


// Class Inheritance
class Calculator {
    add(a, b) {
        return a + b;
    }
    Subtraction(a,b){
        return a-b;
    }
    multiply(a, b) {
        return a * b;
    }

    divide(a, b) {
        if (b === 0) {
            throw new Error("Division by zero is not allowed.");
        }
        return a / b;
    }
}

class Total {
    sum(a, b, c, d, e) {
        return a + b + c + d + e;
    }
}

class PercentageCalculator extends Total {
    percentage(a, b, c, d, e) {
        const total = this.sum(a, b, c, d, e);
        const percentage = (total / 500) * 100;
        return percentage;
    }

}

a=new PercentageCalculator()
b=a.percentage(50,80,60,80,80)
console.log(b)



