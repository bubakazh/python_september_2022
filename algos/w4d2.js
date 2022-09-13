arr = [ 'a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e', 'a']

function makeFreqTable(){
    
    const obj = {}
    for(i = 0; i < arr.length; i++){
        if(obj[arr[i]]){
            obj[arr[i]] += 1;
        }
        else{
            obj[arr[i]] = 1
        }
    }
    console.log(obj)
}

makeFreqTable(arr);  