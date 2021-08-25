// get list of exercises from active workout anc cycle trough it
var divs = document.getElementsByClassName("workout-exercise-single-overlay");


//   document.querySelector(".workout-exercise-single-overlay").addEventListener("click", handleClick)
console.log("js loaded");

function start_workout(){
    console.log(divs.length);




    //itirate trough list of cards with exercises and mark them complete
    for(var i = 0; i < divs.length; i++){
        // divs[i].style.display = "block";
     }
}

//----------------------------------------------------------------------------------------------
var timer_div = document.getElementById("timer_2")
var set_div = document.getElementById("set_2")
timer_div.innerHTML= "Set time: 5"

// //https://stackoverflow.com/questions/21518381/proper-way-to-wait-for-one-function-to-finish-before-continuing

var loops = 2;
var secs = 5;
function firstFunction(){
        if(loops > 0){        
            if(secs<0) {
                        document.getElementById("timer_2").innerHTML="0";
                        console.log('done')
                        secs=5;
                        loops--;
                        
                    }
            document.getElementById("timer_2").innerHTML="Set time: " + secs;
            secs--;
                        
            setTimeout(firstFunction,1000);
        }
        return;
      };


firstFunction()