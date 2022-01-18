let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var n = readLine();
var num = n.toString();
// console.log(num);
var rev_num = num.split('').reverse().join('');
// console.log(rev_num);
if(rev_num == num){
	console.log('True');
} else{
	console.log('False');
}

var n = readLine();
var num = n.toString();
var j = num.length;
let i =0;
while(i<j){
  if (num[i]!== num[j-1]){
    console.log('False')
  }
  i+=1;
  j-=1;
}


// -------- Do NOT edit anything above this line ----------
var num = parseInt(readLine());
let temp = num;
let rem = 0;
let rev_num =0;
while(num!==0){
	rem = num%10;
	num = parseInt(num/10);
	rev_num = rev_num*10 + rem;
}

if (rev_num === temp){
	console.log('True');
} else{
	console.log('False');
}
