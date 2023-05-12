function findQueens(n) {
	// 이곳에 작성합니다.
    var arr = [], answer = 0
    for (let i = 0; i < n; i++) {
        arr.push(0)
    }

    function f(deep, arr){
        if (deep > n){
            answer += 1
            return
        }

        for (let index = 0; index < n; index++) {
            if (arr[index] > 0) continue
            
            let x = false
            for (let i = 0; i < n; i++) {
                if (arr[i] == 0) continue
                if (Math.abs(deep - arr[i]) == Math.abs(index - i)) {
                    x = true
                    break
                }
            }
            if (x) continue
            
            arr[index] = deep
            f(deep + 1, arr)
            arr[index] = 0
        }
    }
    
    f(1, arr)

	return answer
}
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', function(line){
    console.log(findQueens(parseInt(line)))
    rl.close(); // 한 줄 입력받고 종료
}).on('close', function(){
    process.exit();
})