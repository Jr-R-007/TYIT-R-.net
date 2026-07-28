const readline  = require ("readline")
const a1 = readline.createInterface({
    input: process.stdin,
    output:process.stdout

});



    a1.question("Enter your marks to know your grade: ",function(marks){
        marks=Number(marks);
       a1.close
    });


function Grade(marks)
{
    if(marks >= 80){
        console.log("Your grade is O")

    }else if (marks>= 75){
        console.log("Your grade is A+")

    }else if (marks >=60){
        console.log("Your grade is A")
    }else if (marks >=50){
        console.log("Your grade is B+")
    }else if (marks >=40){
        console.log("Your grade is B")
    }else if (marks >=35){
        console.log("You are pass")
    }else {
        console.log("You are Failed")
    }a1.close()
}

