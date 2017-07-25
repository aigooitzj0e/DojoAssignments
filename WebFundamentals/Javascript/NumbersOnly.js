function onlyArr(arr) {
    var arrnew = [];
    for(var idx=0; idx<arr.length; idx++) {
        if(typeof arr[idx] === 'number') {
            arrnew.push(arr[idx]);
        }
    }
    // return newarr;
    console.log(arrnew);
}
onlyArr([1,2,"Dojo",4,5,"Hello", 7, 8, 9]);
