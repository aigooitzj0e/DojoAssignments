function whatTime(HOUR, MINUTE, PERIOD) {
    var timeNew = "";

    if(MINUTE < 30) {
        timeNew = "It's just after " + HOUR;
    }
    if(MINUTE > 30) {
        HOUR += 1;
        timeNew = "It's almost " + HOUR;
    }
    if (MINUTE == 30) {
        timeNew = "Half past " + HOUR;
    }
    if(PERIOD == "AM") {
        timeNew = timeNew + " in the morning.";
    }
    if(PERIOD == "PM") {
        timeNew = timeNew + " in the evening.";
    }
    console.log(timeNew);
}

whatTime(3, 35, "PM");