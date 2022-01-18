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
var prod = 1
while (num!==0){
	n = (num%10);
	sum = sum+n;
	prod = prod*n;
	num = parseInt(num/10);
} 
console.log(prod - sum);