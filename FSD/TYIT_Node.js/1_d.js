let num1=15;
let num2=25;

function add(a,b){
    return a+b;
}

let result=add(num1,num2);

console.log("First Number: " ,num1);
console.log("Second Number: " ,num2);
console.log("Sum : ",result);

const readline = require("readline"); 
const rl=readline.createInterface({
    input:process.stdin,
    output:process.stdout
});     

function displayUserDetails(name,age){
    console.log("\nUser Details");
    console.log("Name:" +name);
    console.log("Age:" +age);
}

rl.question("Enter your name:",function(name){
    rl.question("Enter your age:",function(age){
        displayUserDetails(name,age);
        rl.close();
    });
});