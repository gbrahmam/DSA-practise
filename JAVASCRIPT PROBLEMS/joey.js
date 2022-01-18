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
let total=0;
for(let i=0;i<n;i++){
	val=parseInt(readLine());
	total+=val;
}
let avg = parseInt(total/n);
console.log(avg);
if(avg<25){
	console.log('True');
}else{
	console.log('False');
}