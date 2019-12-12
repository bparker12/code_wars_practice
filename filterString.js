// In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

// Example
// filter_list([1,2,'a','b']) == [1,2]
// filter_list([1,'a','b',0,15]) == [1,0,15]
// filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

function TestType(arg){
    return function(num){
        return Object(num) instanceof arg
    }
}

function filter_list(arr) {
    newArr = arr.filter(TestType(Number))
    console.log(newArr)
}

filter_list([1,2,'a','b'])
filter_list([1,'a','b',0,15])
filter_list([1,2,'aasf','1','123',123])


function filter_list2(arr) {
    let newArr = []
    arr.filter(num => {
        if(Object(num) instanceof Number){
            newArr.push(num)
        }
    })
    console.log("answer", newArr)
}

filter_list2([1,2,'a','b'])
filter_list2([1,'a','b',0,15])
filter_list2([1,2,'aasf','1','123',123])