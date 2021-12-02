/*
Advent of Code 2020, Day 2
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

function solve_A(strings){
    var valids = 0;
    for (line of strings){
        // [n]umber, [c]har, [s]tring
        var [n, c, s] = line.split(' ');

        var [nMin, nMax] = n.split('-');
        nMin = parseInt(nMin);
        nMax = parseInt(nMax);

        c = c.replace(':', '');
        
        // password rule, see problem
        var count = s.split(c).length - 1;

        if (count >= nMin && count <= nMax){
            valids += 1;
        };
    };
    return valids;
};

function solve_B(strings){
    var valids = 0;
    for (line of strings){
        // [n]umber, [c]har, [s]tring
        var [n, c, s] = line.split(' ');

        var [nMin, nMax] = n.split('-');
        nMin = parseInt(nMin);
        nMax = parseInt(nMax);

        c = c.replace(':', '');
        
        // updated password rule, see problem
        var count = (s[nMin-1] == c) + (s[nMax-1] == c);

        if (count == 1){
            valids += 1;
        };
    };
    return valids;
};

let data = read_input("input/2");
console.log("A:" + solve_A(data));
console.log("B:" + solve_B(data));