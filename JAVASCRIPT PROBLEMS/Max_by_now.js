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
let cur_max = parseInt(readLine());
console.log(cur_max);
for(let i=0;i<n-1;i++){
	val = parseInt(readLine());
	cur_max = Math.max(val,cur_max);
	console.log(cur_max);
}