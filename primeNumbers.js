console.log("hello");

function isPrime(num) {
  let prime = [];
  for (let i = 0; i <= num; i++) {
    if ((num / i) % 1 === 0) {
      prime.push(i);
    }
  }
  if ((prime[0] === 1) & (prime[1] === num)) {
    console.log(true);
  } else {
    console.log(false);
  }
}

isPrime(0);

function isPrime2(num) {
  if (num === 1){
    return false
  }else if(num === 2){
    return true
  } else if( num <= 0){
      return false;
  } else {
    for (var i = 2; i < num; i++) {
      if (num % i === 0) {
        return false
        break
      }
    }
    return true
  }
}

console.log("2", isPrime2(1))
