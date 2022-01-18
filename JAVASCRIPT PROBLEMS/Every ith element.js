let fs = require("fs");
let data = fs.readFileSync(0, 'utf-8');
let idx = 0;
data = data.split('\n');

function readLine() {
  idx++;
  return data[idx - 1];
}

// -------- Do NOT edit anything above this line ----------
let l = [];
let n = parseInt(readLine());
for (i=0;i<n;i++){
    l.push(parseInt(readLine()));
}
let k = parseInt(readLine());
let s = 0;
for (i=k-1; i<n; i = i+k){
    s += l[i];
}
console.log(s);