function rangePrint(start, end, skip) {
    if (start > end) {
        console.log("Your START number cannot be bigger than your END number!");
    }
    for(var i = start; i <= end; i += skip) {
        console.log(i);
    }
}

rangePrint(2, 20, 2);