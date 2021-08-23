//get list of exercises from active workout anc cycle trough it
var divs = document.getElementsByClassName("workout-exercise-single-overlay");
for(var i = 0; i < divs.length; i++){
    //do something to each div like
    // divs[i].innerHTML = "<i class="fab fa-accusoft"></i>";
    divs[i].style.display = "block";
 }


 document.querySelector('.workout-exercise-single-wrapper').click();