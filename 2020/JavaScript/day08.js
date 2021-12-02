/*
Advent of Code 2020, Day 5
JavaScript
Rico van Midde
*/

function read_input(file){
    var fs = require("fs");

    // file to strings
    var stringData = fs.readFileSync(file).toString().split('\n');
    console.log(stringData);

    return stringData;
}

function solve_A(x){
    return null;
};

function solve_B(x){
    return null;
};

let data = read_input("input/5");
console.log("A:" + solve_A(data));
console.log("B:" + solve_B(data));