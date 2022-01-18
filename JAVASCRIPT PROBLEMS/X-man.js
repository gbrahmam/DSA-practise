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
	let n=parseInt(readLine());
	let arr = readLine().split(' ');
	let total=0;
	for(let j=0;j<n;j++){
		total+=parseInt(arr[j]);
	}
// 	console.log(total);
	let avg = total/n;
// 	console.log(avg);
	let count=0;
	for(let k=0;k<n;k++){
		if(parseInt(arr[k])>avg){
			count+=1;
		}
	}
	console.log(count);
}