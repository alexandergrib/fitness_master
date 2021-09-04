// get list of exercises from active workout anc cycle trough it
let cards_divs = document.getElementsByClassName("col-wrapper-single-exercise");
// var finish_divs = document.getElementsByClassName("workout-exercise-single-overlay");
let hidden_inputs = document.getElementsByClassName("hidden_inputs");
//   document.querySelector(".workout-exercise-single-overlay").addEventListener("click", handleClick)

console.log("js loaded");


function addNewInput(id, repsVal, weightVal){
    // <input type="hidden" name="info_{{ exercise._id }}[]" value="REP15 @ 5kg" />
    const newInput = document.createElement("input");
    newInput.setAttribute("type", "hidden");
    newInput.setAttribute("name", `info_${id}[]`);
    newInput.setAttribute("value", `${repsVal},${weightVal}`);
    // console.log(newInput);
    return newInput
} 

function submitMyForm(id){
    let form = document.getElementById(id);
    console.log('form submitted');
    // console.log(id);
    form.submit(); //this dont work
}

function handleSubmit(event){
    event.preventDefault();  
    console.log('input added');
    let id = this.elements[2].name.replace('id_','');
    let repsVal = this.elements[0].value;
    let weightVal = this.elements[1].value;
    let responce = addNewInput(id, repsVal, weightVal);
    children =this.querySelector('.hidden_inputs');
    // console.log(children);
    children.appendChild(responce);
    // this.submit();  //this works
    let saveCompletedData = document.getElementById(`save_completed_id_${id}`)
    let newLi = document.createElement("li");
    newLi.appendChild(document.createTextNode(`${repsVal} REPS @ ${weightVal}kg`));
    // saveCompletedData.appendChild(newLi);
    saveCompletedData.insertBefore(newLi, saveCompletedData.lastChild);
    
}


let form = document.getElementsByTagName('form');
for(i=0; i< form.length; i++){
    form[i].addEventListener('submit', handleSubmit);
}    



