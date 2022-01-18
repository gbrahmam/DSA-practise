let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let arr = readLine().split(" ");
let ev_arr = [];
let od_arr = [];
for(let i =0;i<arr.length;i++){
	if (parseInt(arr[i])%2===0){
		ev_arr.push(parseInt(arr[i]));
	}else{
		od_arr.push(parseInt(arr[i]));
	}
}
res = od_arr.concat(ev_arr);
console.log(...res);