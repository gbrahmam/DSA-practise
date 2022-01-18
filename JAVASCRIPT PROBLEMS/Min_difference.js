let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let n=parseInt(readLine());
let arr = readLine().split(' ');
let min_diff = Infinity;
arr.sort(function(a,b){return (a-b)});
for(let i=1;i<n-1;i++){
	min_diff = Math.min(min_diff,(parseInt(arr[i+1]-parseInt(arr[i]))));
}
console.log(min_diff);