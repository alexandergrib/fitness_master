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
timer_div.innerHTML= "2 min /  01.00.12"
// var start = Date.now();
// setInterval(function() {
//     var delta = Date.now() - start; // milliseconds elapsed since start
//     …
//     output(Math.floor(delta / 1000)); // in seconds
//     // alternatively just show wall clock time:
//     output(new Date().toUTCString());
// }, 1000); // update about every second
// div id="timer_2"

// let counter = 0;
// const intervalId = setInterval(() => {

//     // console.log('Hello World');

//     counter += 1;
//     if (counter === 5) {
//         console.log('Done');
//         divs[0].style.display = "block"; 
//         clearInterval(intervalId);
//     }
// }, 1000);

// var ticks = 20;
// // setTimeout(sayHi, 1000);
// //https://stackoverflow.com/questions/21518381/proper-way-to-wait-for-one-function-to-finish-before-continuing
// //counter
// async function firstFunction(){
    
//     if(ticks<0) {
//                 document.getElementById("timer_2").innerHTML="0";
//                 return;
//             }
//     document.getElementById("timer_2").innerHTML=ticks;
//     ticks--;
                
//     setTimeout(firstFunction,1000);

//     // return;
//   };

// //   then use await in your other function to wait for it to return:
//   //itirator trough cycles
// async function secondFunction(){

//     await firstFunction();
//     console.log("second fun call")

   
//     // now wait for firstFunction to finish...
//     // do something else
    
//   };



//   secondFunction();

// // setTimeout(updateCount, 1);
// var ticks = 0;
// let elementId = "timer_2";
// function countDownTimer(elementId, ticks) {
    
//     if(ticks<0) {
//         document.getElementById(elementId).innerHTML="0";
//         return;
//     }
  
//     document.getElementById(elementId).innerHTML=ticks;
//     ticks--;
    
//     setTimeout(countDownTimer,1000);
//   }


// countDownTimer(elementId, 150);
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
            document.getElementById("timer_2").innerHTML="2 min / " + secs;
            console.log(loops);
            console.log(secs);
            secs--;
                        
            setTimeout(firstFunction,1000);
        }
        return;
      };


firstFunction()