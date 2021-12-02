/*
Advent of Code 2020, Day 1
JavaScript
Rico van Midde
*/

function read_input(file){
    var fs = require("fs");

    // file to strings
    var stringData = fs.readFileSync(file).toString().split('\n');

    // strings to ints
    var intData = stringData.map(function (x) { 
        return parseInt(x, 10); 
      });

    return intData
}

function solve_A(numbers){
    for (let a of numbers){
        for (let b of numbers){
            if (a + b == 2020){return a*b}
        }
    }
}

function solve_B(numbers){
    for (let a of numbers){
        for (let b of numbers){
            for (let c of numbers){
                if (a + b + c == 2020){return a*b*c}
            }
        }
    }
}

let numbers = read_input("input/1")
console.log("A:" + solve_A(numbers));
console.log("B:" + solve_B(numbers));