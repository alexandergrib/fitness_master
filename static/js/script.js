/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function () {
    $(".sidenav").sidenav({edge: "left"});
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $("select").formSelect();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 3,
        showClearBtn: true,
        i18n: {
            done: "Select"
        } 
    });

    /*
        insert new li item in exercise html
    */
    var li_count = 2;
    $('#add_more').click(function(){
        li_count += 1;
        // alert("clicked");        
        $("#steps_list li:last").before(
            "<li> <i class='fas fa-pencil-alt prefix light-blue-text text-darken-4'></i>" +
             "<input id=step" + li_count + " name='steps' minlength='3' maxlength='1500'"+
                              " type='text' class='validate' >"+
                            "<label for=step"+li_count+">Step "+ li_count + "</label> </li>"
        );
    });
});

