const { stdout } = require("process")
const Readline = require("readline")

const r1=readline.createinterface({
    input:stdin,
    output:stdout
})

let studets=[]

function addstudent(name,rollno,marks){
    let students={
    name=name,
    rollno=rollno,
    marks=marks
};
students.push(students)
}



