

function findOdd(A) {
  let storeNum = 0
  // A.map(num => {
    for(let i=0;i < A.length; i++){
      // A.filter(num => {
      //   if(num = i){
      //     storeNum++
      //     if(Number.isInteger(storeNum/2))
      //       // console.log("num", num)
      //   }
      // })
      // })
    }
    // console.log(storeNum)
}

const arr1 = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]

findOdd(arr1)


const num = 5.5

// console.log("int check", Number.isInteger(num))

// function doTest(a, n) {
//   console.log("A = ", a);
//   console.log("n = ", n);
//   Test.assertEquals(findOdd(a), n);
// }
// Test.describe('Example tests', function () {
//   doTest([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5);
//   doTest([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5], -1);
//   doTest([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5], 5);
//   doTest([10], 10);
// })