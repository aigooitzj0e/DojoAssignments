function fewBillion () {
    var wallet = 1;
    for(var day = 2; day <= 30; day++) {
        wallet = wallet * 2;

    console.log("Day: " + day,"--", "Dollars: " + wallet/100,"--", "Pennies: " + wallet);
    }
}

fewBillion();