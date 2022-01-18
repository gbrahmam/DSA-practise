let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let n = parseInt(readLine());
let max = -Infinity;
let min = Infinity;
for(let i = 0;i<n;i++){
	val = parseInt(readLine());
	min = Math.min(min,val);
	max = Math.max(val,max);
}
console.log(max);
console.log(min);