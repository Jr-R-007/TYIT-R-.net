let num1=10;
let num2=15;

console.log("Arithmetic Operators")
console.log("Addition of "+(num1) + "\tand " + (num2)+ "\tis " +(num1 + num2) );
console.log("Substraction of "+(num1) + "\tand " + (num2)+ "\tis " +(num1 - num2) );
console.log("Multiplication of "+(num1) + "\tand " + (num2)+ "\tis " +(num1 * num2) );
console.log("Division of "+(num1) + "\tand " + (num2)+ "\tis " +(num1 / num2) );

console.log("Relational  Operators and control statments")
if (num1 > num2){
    console.log(num1 +" is greater than " +num2 )
}else if (num1< num2){
    console.log(num1 +" is less than " +num2 )
}else{
    console.log(num1 +" are both equal " +num2 )
}

//By taking input from user
const readline=require("readline")
const r1 = readline.createInterface({
    input:process.stdin,
    output:process.stdout

})