/*jshint esversion: 6 */
// get list of exercises from active workout anc cycle trough it
let cards_divs = document.getElementsByClassName("col-wrapper-single-exercise");
let hidden_inputs = document.getElementsByClassName("hidden_inputs");

function addNewInput(id, repsVal, weightVal){
    const newInput = document.createElement("input");
    newInput.setAttribute("type", "hidden");
    newInput.setAttribute("name", `info_${id}[]`);
    newInput.setAttribute("value", `${repsVal},${weightVal}`);
    return newInput;
} 

function submitMyForm(id){
    let form = document.getElementById(id);
    form.submit();
}

function handleSubmit(event){
    event.preventDefault();
    let id = this.elements[2].name.replace('id_','');
    let repsVal = this.elements[0].value;
    let weightVal = this.elements[1].value;
    let responce = addNewInput(id, repsVal, weightVal);
    let children =this.querySelector('.hidden_inputs');
    children.appendChild(responce);
    let saveCompletedData = document.getElementById(`save_completed_id_${id}`);
    let newLi = document.createElement("li");
    newLi.appendChild(document.createTextNode(`${repsVal} REPS @ ${weightVal}kg`));
    saveCompletedData.insertBefore(newLi, saveCompletedData.lastChild);
}

let form = document.getElementsByTagName('form');
for(let i=0; i< form.length; i++){
    form[i].addEventListener('submit', handleSubmit);
}    

