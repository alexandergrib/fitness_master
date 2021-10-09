/*jshint esversion: 6 */
//example from here https://stackoverflow.com/questions/18076013/setting-session-variable-using-javascript
let workoutSwitch = document.getElementById('show_completed');
let completedDivs = document.getElementsByClassName("completed");

function handleWorkoutSwitch(){
    if (workoutSwitch.checked === true){
        localStorage.setItem("workoutCheckBox", "true");
        // completedDivs[0].style.display="none";
        for (let i=0; i < completedDivs.length; i++){
            completedDivs[i].style.display="block";
        }
    } else {
        localStorage.setItem("workoutCheckBox", "false");
        for (let i=0; i < completedDivs.length; i++){
            completedDivs[i].style.display = 'none';
        }
    }
}

if (localStorage.getItem("workoutCheckBox")) {
    workoutSwitch.checked = eval(localStorage.getItem("workoutCheckBox"));
    if (workoutSwitch.checked === true){
        for (let i=0; i < completedDivs.length; i++){
            completedDivs[i].style.display = 'block';
        }
    }else {
        for (let i = 0; i < completedDivs.length; i++) {
            completedDivs[i].style.display = 'none';
        }
    }
}else {
    workoutSwitch.checked = true;
    for (let i=0; i < completedDivs.length; i++){
            completedDivs[i].style.display = 'block';
        }
}

