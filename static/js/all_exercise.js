/*jshint esversion: 6 */

/*
Toggle switch to show all exercises or only created by user
exercise_all.html
*/
let systemExercisesSwitch = document.getElementById('system_exercises');
let adminExercisesDiv = document.getElementsByClassName("admin-exercises");

if (localStorage.getItem("adminCheckbox")){
    systemExercisesSwitch.checked =  eval(localStorage.getItem("adminCheckbox"));  

} else {
    systemExercisesSwitch.checked = true;
}

if (systemExercisesSwitch.checked === false){
    adminExercisesDiv[0].style.display="none";
} else {
    adminExercisesDiv[0].style.display = 'block';
}

function hideSystemExercises() {
    if (systemExercisesSwitch.checked === true){
        localStorage.setItem("adminCheckbox", true);
        adminExercisesDiv[0].style.display="block";
    } else {
        adminExercisesDiv[0].style.display = 'none';
        localStorage.setItem("adminCheckbox", false);
    }

}
