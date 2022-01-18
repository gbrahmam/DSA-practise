let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------

function difference_sum_even_odd_index(arr){
	if (arr.length === 1){
		return parseInt(arr[0]);
	}
	let n = arr.length;
	let ev_sum = 0;
	let od_sum = 0;
	for(let i = 2;i<=n;i+=2){
		ev_sum+=parseInt(arr[i-2]);
		od_sum+=parseInt(arr[i-1]);
	}
	if (n%2!==0){
		ev_sum+=parseInt(arr[n-1]);
	}
	let diff = ev_sum - od_sum;
	return diff;
}

let arr = readLine().split(" ");
res = difference_sum_even_odd_index(arr);
console.log(res);