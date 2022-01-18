let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var text = readLine();
// var text = "hello"
var array = text.trim().split(' ');
  //var last = array[array.length - 1]
  // console.log(last)
var len = array[array.length -1].length;
console.log(len);