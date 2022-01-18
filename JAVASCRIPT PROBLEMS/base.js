let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let t=parseInt(readLine());
for(let i=0;i<t;i++){
	let summ = 0;
	let n = parseInt(readLine());
	let arr = readLine().split(' ');
	for(let j=0;j<(n);j++){
		summ+=parseInt(arr[j]);
	}
	let limit = parseInt(summ/n);
	for(let k=0;k<(n);k++){
		if (limit<=parseInt(arr[k])){
			arr[k]= parseInt(arr[k])-limit;
		}else{
		    arr[k]=parseInt(arr[k]);
		}
	}
	console.log(...arr);
}