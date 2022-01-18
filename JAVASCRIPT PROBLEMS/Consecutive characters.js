let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
var word = readLine();
var array = word.split('');
var len = array.length;
var maxlen = 0;
var count = 1;
for (var i=1;i<len;i++){
	if (array[i]==array[i-1]){
		count+=1;
	} else {
		maxlen = Math.max(maxlen,count);
		count = 1;
	}
}
if (count>maxlen){
	maxlen = count;
}
console.log(maxlen)