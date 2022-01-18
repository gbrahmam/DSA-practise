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
	val = parseInt(readLine());
	arr.push(val);
}
let x =parseInt(readLine());
let space=0;
for(let j=0;j<n;j++){
	if(arr[j]<x){
		space+=arr[j];
	}
}
console.log(space);