var daysUntilMyBirthday = 80;
while (daysUntilMyBirthday >= 0) {
    console.log(daysUntilMyBirthday);
    if(daysUntilMyBirthday > 30) {
        console.log("Such a long time... :(");
    }
    if (daysUntilMyBirthday <= 30) {
        console.log("DAYS UNTIL MY BIRTHDAY!!!");
    }
    if (daysUntilMyBirthday == 0) {
        console.log("♪ღ♪░H░A░P░P░Y░ B░I░R░T░H░D░A░Y░░♪ღ♪");
    }
    daysUntilMyBirthday = daysUntilMyBirthday - 1;
}