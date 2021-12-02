/*
Advent of Code 2020, Day 4
JavaScript
Rico van Midde
*/
const { checkPrime } = require("crypto");
const fs = require("fs");

function read_input(file){
    // file to strings
    var stringData = fs.readFileSync(file).toString().split('\n');
    // console.log(stringData);

    // seperate passports
    var documents = []
    var passport = {}
    for (line of stringData){

        // go to next passport
        if (line == ''){
            documents.push(passport);
            passport = {}
            continue
        }

        // add entries of line to passport
        for (entry of line.split(' ')){
            var [key, value] = entry.split(':')

            // ignore 'cid' entry
            if (key == 'cid'){continue}
            passport[key] = value
        }
    }

    // console.log(documents);
    return documents;
}

function solve_A(documents){
    // count valid passports
    var count = 0
    for (passport of documents){
        if (Object.keys(passport).length == 7){count++}
    }
    return count;
};

const check = {
    'byr':function(s){return (parseInt(s) >= 1920 && parseInt(s) <= 2002)},
    'iyr':function(s){return (parseInt(s) >= 2010 && parseInt(s) <= 2020)},
    'eyr':function(s){return (parseInt(s) >= 2020 && parseInt(s) <= 2030)},
    'hgt':function(s){
        var n = parseInt(s)
        return (s.slice(-2) == 'cm') ? (n>=150 && n <=193) : (n>=59 && n <=76)
    },
    'hcl':function(s){
        if (s[0] != '#' || s.length != 7){return false}
        for (i = 1; i < 7; i++){if(!"0123456789abcdef".includes(s[i])){return false}}
        return true
    },
    'ecl':function(s){return ['amb', 'blu','brn','gry','grn','hzl','oth'].includes(s)},
    'pid':function(s){return (s.length == 9 && !isNaN(s))}
}

function solve_B(documents){
    // count valid passports
    var count = 0
    for (passport of documents){
        if (Object.keys(passport).length == 7){
            count++
            for (key in passport){
                value = passport[key]                
                if (!check[key](value)){
                    count--
                    break
                }    
            }
        }
    }
    return count;
};

let data = read_input("input/4");
console.log("A:" + solve_A(data));
console.log("B:" + solve_B(data));