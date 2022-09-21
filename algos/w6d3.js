// we're making a function that will give us an object with the least amount of coins for the int amount of change we are given

let cents1 = 25
let cents2 = 10
let cents3 = 96
let cents4 = 0
let cents5 = 69
let cents6 = 32

function makesLeastCents(cents){
    const coinPurse = {}
    const denomination = {
        'quarter' : 25,
        'dime' : 10,
        'nickel' : 5,
        'penny' : 1
    }
    for (coin in denomination){
        if (cents % denomination[coin] == cents){
            continue
        }
        else{}{

            coinPurse[coin] = Math.floor(cents / denomination[coin]);
            var nonCents = cents % denomination[coin];
            cents = nonCents; 
        }
    }
    console.log(coinPurse)
    return coinPurse
}

makesLeastCents(cents1)
makesLeastCents(cents2)
makesLeastCents(cents3)
makesLeastCents(cents4)
makesLeastCents(cents5)
makesLeastCents(cents6)
