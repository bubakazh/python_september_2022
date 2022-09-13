
/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @returns {string} The given array items as a string separated by the given separator.
 */

// TYLER'S METHOD

function join(arr, separator=", "){
    let newStr = ""
    for(i = 0; i < arr.length; i++){
        newStr += arr[i]
        if(i < arr.length - 1){
            newStr += separator
        }
    }
    console.log(newStr)
    return newStr
}

join(arr1, separator1)
join(arr2, separator2)
join(arr3, separator3)
join(arr4, separator4)
join(arr5, separator5)

// MY GROUP'S METHOD

function joiner(arr, separator= ", "){
    let newString = ""
    for(i = 0; i < arr.length; i++){
        newString += arr[i] + separator
    }
    // newString.slice(0,-1)                                                THIS IS NOT HOW IT'S DONE
    newString = newString.slice(0,(newString.length) - separator.length ) //THIS IS HOW IT'S DONE, THANKS TYLER
    console.log(newString)
    return newString
}

joiner(arr1, separator1)
joiner(arr2, separator2)
joiner(arr3, separator3)
joiner(arr4, separator4)
joiner(arr5, separator5)