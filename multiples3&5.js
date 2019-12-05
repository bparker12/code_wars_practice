// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

// Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

// Note: If the number is a multiple of both 3 and 5, only count it once.

function solution(number) {
    // console.log("original number", number)
    let finalSum = 0
    let allNums = []
    for (let num = 1; num < number; num++) {
        if (num % 3 === 0 || num % 5 ===0){
            allNums.push(num)
        } else if(num % 3 === 0){
            allNums.push(num)
        } else if(num % 5 === 0){
            allNums.push(num)
        }
    }
    console.log(allNums)
    allNums.forEach(num => {
        finalSum += num
        console.log("in loop", finalSum)
    })
    console.log(finalSum)
}

solution(10)

function solution2(number) {
    let total = 0
    for (let i =0; i < number; i++){
        if(i % 3 === 0 || i % 5 === 0){
            total += i
        }
    }
    console.log("solution2", total)
}

solution2(10)