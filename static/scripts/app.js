$(document).ready(function(){
    $(".mstart").click(function(){
        $.get("/start");
    });

    $(".mstop").click(function(){
        $.get("/stop");
    });

    $(".astart").click(function(){
        $.get("/light");
    });

    $(".astop").click(function(){
        $.get("/dim");
    });
});