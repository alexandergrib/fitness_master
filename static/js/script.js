/*jshint esversion: 6 */
/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "left"});
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $("select").formSelect();
    $('.tabs').tabs();
    $('.modal').modal();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });

    /*
        insert new li item in create_exercise.html
    */
    var li_count = 2;
    $('#add_more').click(function () {
        li_count += 1;
        $("#steps_list li:last").before(
            "<li style='margin-left:3rem;'><label for=step" + li_count + "><input id=step" +
            li_count + " name='steps' minlength='3' maxlength='1500' type='text' class='validate' required>" +
            " Next Step <i class=' fas fa-minus-circle ' style='color:red; float:right; font-size:1.1rem; cursor: pointer;'> Remove</i></label> </li>"
        );
        $("i.fa-minus-circle").on("click", function (event) {
            $(event.target).closest("li").remove();
        });
    });
});

//hide loading container
document.body.onload = function () {
    document.querySelector(".loading-container").classList.add("hide");
};
