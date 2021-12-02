/*
Advent of Code 2020, Day 6
JavaScript
Rico van Midde
*/
const fs = require("fs");

function read_input(file){

    // file to strings
    let stringData = fs.readFileSync(file).toString().split('\n');
    console.log(stringData);

    return stringData;
}

function solve_A(stringData){
    // sum unique answers per group
    let count = 0
    let answers = []
    for (s of stringData){
        // switch to next group
        if (s == ''){
            let uniqueAnswers = [... new Set(answers)]
            count += uniqueAnswers.length
            answers = []
            continue
        }

        // update group
        answers.push(...s)
    }
    return count
};

function solve_B(stringData){
        // sum overlapping answers per group
        let count = 0
        let answers = []
        let stupidSwitch = true
        for (s of stringData){
            // switch to next group
            if (s == ''){
                count += answers.length
                // console.log(answers)
                answers = []
                stupidSwitch = true
                continue
            }
    
            // update group
            if (answers.length == 0 && stupidSwitch){
                answers = [...s]
                stupidSwitch = false
            } else {
                // finds intersection
                answers = answers.filter(x=>[...s].includes(x));
            }
        }
        return count
};

let data = read_input("input/6");
console.log("A:" + solve_A(data));
console.log("B:" + solve_B(data));