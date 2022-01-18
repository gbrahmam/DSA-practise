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
let arr = [];
for(let i=0;i<n;i++){
	val = readLine();
	arr.push(val);
}
for(let j=0;j<n;j++){
	console.log(j+ " " +arr[j]);
}