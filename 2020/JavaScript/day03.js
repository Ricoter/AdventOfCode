/*
Advent of Code 2020, Day 3
JavaScript
Rico van Midde
*/

const { count } = require("console");

function read_input(file){
    var fs = require("fs");

    // file to strings
    var stringData = fs.readFileSync(file).toString().split('\n');
    console.log(stringData);

    return stringData;
}

function solve_A(stringData){
    var L = stringData[0].length;
    var count = 0;
    var x = 0 // horizontal coordinate

    for (line of stringData){
        if (line[x%L] == '#'){count += 1};
        x += 3
    };
    return count;
};

function countTrees(stringData, slope){
    var L = stringData[0].length;
    var count = 0
    var x = 0 // horizontal coordinate
    var y = 0 // vertical coordinate
    while (y < stringData.length){
        if (stringData[y][x%L] == '#'){
            count += 1
        };
        x += slope[0]
        y += slope[1]
    }
    return count;
};

function solve_B(stringData){
    var count = 1
    for (slope of [[1,1], [3,1], [5,1], [7,1], [1,2]]){
        count *= countTrees(stringData, slope);
    };
    return count;
};

let data = read_input("input/3");
console.log("A:" + solve_A(data));
console.log("B:" + solve_B(data));