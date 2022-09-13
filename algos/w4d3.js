// Given a String, return it without duplicates.

const str1 = "abcABC"
const str2 = "helloo"

function strDeDupe(str){

    const obj = {}
    
    let newStr = ""
    
    for(i = 0; i < str.length; i++){
    //     obj[str[i]] = 1
    //     if (obj[str[i]] === 1){
    //         new_string += str[i]
    //     }
    //     else{
    //         continue
    //     }
    // }                                      for the first attempt, we just had a couple things a little bit backwards...
        if(obj[str[i]]){
            continue
        }
        else{
            newStr += str[i]
            obj[str[i]] = 1
        }
    }
    console.log(newStr)
    return newStr
}

strDeDupe(str1)
strDeDupe(str2)
