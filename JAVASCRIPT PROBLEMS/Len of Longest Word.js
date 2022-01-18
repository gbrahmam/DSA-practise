let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var word = readLine();
var array = word.trim().split(' ');
var maximum = 0
for (i=0;i<array.length;i++) {
	if (array[i].length>maximum){
		maximum = array[i].length
	}
}
console.log(maximum)