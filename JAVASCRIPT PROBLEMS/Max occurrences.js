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
if (n===0){
	console.log(0)
}else{
// console.log(arr)
let count_arr = [];
for(let i=0;i<n;i++){
	let count=1;
	for(let j=i+1;j<n;j++){
		if(arr[j]===arr[i]){
			count=count+1;
		}
	}count_arr.push(count);
}
let maxx = Math.max(...count_arr);

for(let k=0;k<n;k++){
	if(count_arr[k]===maxx){
		console.log(arr[k])
	}
}
}




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
if (n===0){
	console.log(0);
}else{
let count = 1;
let res = -1;
for(let i = 1;i<n;i++){
	if(arr[i]===arr[i-1]){
		count+=1;
	}else{
		res = Math.max(res,count);
		count=1;
	}
}
res = Math.max(res,count);
count = 1;
for(let j = 1;j<n;j++){
	if(arr[j]===arr[j-1]){
		count+=1;
	}else{
		if (count===res){
			console.log(arr[j-1]);
		}
		count=1
	}
}
if (count===res){
	console.log(arr[n-1]);
}
if (res===-1){
	console.log(-1);
}
}