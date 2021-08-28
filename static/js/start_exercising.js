// get list of exercises from active workout anc cycle trough it
let cards_divs = document.getElementsByClassName("col-wrapper-single-exercise");
// var finish_divs = document.getElementsByClassName("workout-exercise-single-overlay");
var hidden_inputs = document.getElementsByClassName("hidden_inputs");
//   document.querySelector(".workout-exercise-single-overlay").addEventListener("click", handleClick)
console.log("js loaded");


function handleSubmit(event){
    event.preventDefault();
    // form.submit();
    console.log('form submitted');
}


let form = document.getElementsByTagName('form');
for(i=0; i< form.length; i++){
    form[i].addEventListener('submit', handleSubmit);
}    




function boxClicked(){
    if (this.style.backgroundColor === "orange") {
        this.style.backgroundColor = "green";
    } 
    else {
        this.style.backgroundColor = "orange";
    }
    

}



    //itirate trough list of cards with exercises and mark them complete
for(var i = 0; i < cards_divs.length; i++){
        // divs[i].style.display = "block";
        cards_divs[i].addEventListener('click', boxClicked);
        
     }
