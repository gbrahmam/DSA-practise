process.stdin.resume();
process.stdin.setEncoding('utf8');

// your code goes here

let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let t = parseInt(readLine());
for(let i=0;i<t;i++){
	let arr = readLine().split(' ');
	let a = parseInt(arr[0]);
	let d1 = parseInt(arr[1]);
	let b = parseInt(arr[2]);
	let d2 = parseInt(arr[3]);
	if (d2>d1){
	    console.log('NO');
	}else{
    	let n = ((a-b)%(d2-d1));
        // console.log(n);
        if(n===0){
        	console.log('YES');
        }else{
        	console.log('NO');	
	}
	}
}

