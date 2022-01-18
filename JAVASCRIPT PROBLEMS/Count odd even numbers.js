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
od_count = 0;
ev_count = 0;
for(let i = 0;i<n;i++){
	val = parseInt(readLine());
	if (val%2===0) ev_count+=1;
	else od_count+=1;
}
console.log(od_count);
console.log(ev_count);