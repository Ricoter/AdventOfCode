/*
Advent of Code 2020, Day 5
JavaScript
Rico van Midde
*/
const fs = require("fs");

function read_input(file){
    // file to strings
    var stringData = fs.readFileSync(file).toString().split('\n');
    console.log(stringData);

    return stringData;
}

function seatID(s){
    // to binary
    var row = s.substr(0,7).replace(/B/g, '1').replace(/F/g, '0')
    var seat = s.substr(7,10).replace(/R/g, '1').replace(/L/g, '0')

    // return decimal seat ID
    return parseInt(row, 2) * 8 + parseInt(seat, 2)
}

function solve_A(stringData){
    return Math.max(...(stringData.map(seatID)));
};

function solve_B(stringData){
    var taken = stringData.map(seatID)
    var max = Math.max(...taken)
    var min = Math.min(...taken)
    for (i=min; i<max; i++){if(!taken.includes(i)){return i}}
};

let data = read_input("input/5");
console.log("A:" + solve_A(data));
console.log("B:" + solve_B(data));