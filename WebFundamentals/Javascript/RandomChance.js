function randomChance(quarterNum) {
    // var quarterNum = 20;
    var randomNum = Math.floor(Math.random() * 100 + 1);
    var winningNum = Math.floor(Math.random() * 100 + 1);
    var winningAmt = Math.floor(Math.random() * 51) + 50;
    var wallet = quarterNum;

    while(wallet >= 1) {
        if(randomNum == winningNum) {
            console.log("WINNER! You won ", winningAmt, "quarters!");
            wallet = wallet + winningAmt;
            console.log("You have ", wallet, "quarters!");
            wallet--;
            return wallet;
        }
        else{
            wallet--;
            console.log("Using another credit. Balance is now: ", wallet);
            console.log("Your number is ", randomNum, "The winning number was ", winningNum);
            randomNum = Math.floor(Math.random() * 100);
            winningNum = Math.floor(Math.random() * 100);
            winningAmt = Math.floor(Math.random() * 50) + 51;
        }
    }
    console.log(wallet);

    if(wallet == 0) {
        console.log("Out of Quarters, Thanks for Playing!");
    }
}

randomChance(100);