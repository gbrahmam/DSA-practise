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
for(let i = 0;i<n;i++){
	val = parseInt(readLine());
	arr.push(val);
}
let k = parseInt(readLine());
let j =0;
let add = 0;
while (j<n){
	if (arr[j]%k === 0){
		add+=arr[j];
	}
	j+=1;
}
console.log(add);