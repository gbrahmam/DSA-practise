let n = parseInt(readLine());
let maxx = parseInt(readLine());
let m = parseInt(readLine());
let dials = new Array(n).fill(0);
for(var j=0; j<m;j++){
	val = parseInt(readLine())-1;
	dials[val]+=1;
	//console.log(dials)
	if (dials[val]===max){
		console.log(val);
		break;
	}
}