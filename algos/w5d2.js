/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str){
    let valid = true
    const counter = {}
    counter["("] = 0
    counter[")"] = 0
    for(i = 0; i < str.length; i++){
        console.log(counter)
        if(str[i] == "("){
            counter["("] += 1;
        }
        if(str[i] == ")"){
            counter[")"] += 1;
        }
        if(str[i] == ")" && counter["("] == 0){
            valid = false
            return valid 
        }
        if(counter[")"] > counter["("]){
            valid = false
            return valid
        }
    }
    if(counter["("] !== counter[")"]){
        valid = false
        return valid
    }
    return valid
}

console.log(parensValid(str1))
console.log(parensValid(str2))
console.log(parensValid(str3))
console.log(parensValid(str4))
console.log(parensValid(")"))



// function validParens(str){
//     let count = 0
//     for(let i of str){
//         console.log(i)
//         if(i === ")"){
//             count--
//             if(i ===")" && count < 0){
//                 return false
//             }
//         }
//         else if(i === "("){
//             count++
//         }
//         console.log(count)
//     }
//     return (count === 0)
// }

// console.log(validParens(str1))
// console.log(validParens(str2))
// console.log(validParens(str3))
// console.log(validParens(str4))
// console.log(validParens(")"))