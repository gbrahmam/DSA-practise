let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let test = parseInt(readLine());
for(let i = 0;i<test;i++){
	let arr1 = readLine().split(' ');
	let arr2 = readLine().split(' ');
	let x = Math.min(arr1.length,arr2.length);
	let y = Math.max(arr1.length,arr2.length);
	// console.log(arr1,arr2);
	// console.log(x,y);
	let cary = 0;
	let res =[];
	let sum = 0;
	for(let j =0;j<x;j++){
	  sum = parseInt(arr1[j]) + parseInt(arr2[j]) + cary;
	  res.push(sum%10);
	  cary = parseInt(sum/10);
	}
	// console.log(res);
	if (arr1.length>arr2.length){
	  arr2 = arr1;
	}
	for (let k =x;k<y;k++){
	  sum = parseInt(arr2[k])+cary;
	  res.push(sum%10);
	  cary = parseInt(sum/10);
	}
	if (cary!==0){
		res.push(cary);
	}
	console.log(res.join(''));
}