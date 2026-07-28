//Function  calling
const readline= require("readline");
const r1=readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
function displayresult(){
    console.log("=======================");
    console.log(" Calculate total marks ");
    console.log("=======================");
}
function total_mark(m1,m2,m3){
    return m1+m2+m3;
}
function calculatet_percentage(total){
    return total/3;
}
function total_grade(marks){
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
       }
    }
}
function studet_details(name,rollno,total,percentage,grade){

    console.log("Enter your name",name);
    console.log("Enter your roll no",rollno);
    console.log("Your Total marks are :" +total +"/300");
    console.log("Your Percentage of total marks are: "+percentage.toFixed(2) + "%");
    console.log("You awarded with grade" +grade);
}

displayresult();
r1.question("Enter your name :",function(name){
    r1.question("Enter your roll number :",function(rollno){
        r1.question("Enter your first subject marks",function(sub1){
            r1.question("Enter your second subject marks",function(sub2){
                r1.question("Enter your third and final subject marks",function(sub3)
                {

                    let m1=Number(sub1);
                    let m2=Number(sub2);
                    let m3=Number(sub3);


                    let total=totalmark(m1,m2,m3);
                    let percentage=calculatet_percentage(total);
                    let grade=total_grade(percentage);
                    studet_details(name,rollno,total,percentage,grade);

                    

                    r1.close();
                });
            });
        });
    });
});
