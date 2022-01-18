let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var num = readLine();
var sum = 0;
while (num!==0){
	n = (num%10);
	sum = (sum*10)+n;
	num = parseInt(num/10);
} 
console.log(sum);