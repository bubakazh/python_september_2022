goFast = "racecar"
almost = "laconical"

function paliChecker(str){
    let palindrome = true
    for(i = 0; i < Math.floor(str.length/2); i++){
        if (str[i] != str[str .length - 1 - i]){
            palindrome = false
        }
    }
    console.log(palindrome)
    return palindrome
}

paliChecker(goFast)
paliChecker(almost)