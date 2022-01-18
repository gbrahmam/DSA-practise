let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
function sum_frst_n(N){
	if (N===1) return 1;
	return N + sum_frst_n(N-1);
}
let n = parseInt(readLine());
res = sum_frst_n(n);
console.log(res);