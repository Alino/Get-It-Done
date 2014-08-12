$(document).ready(function() {

    $("#buttonNewTodo").click(function() {
        $(".search").hide();
        $("#inputNewTag").hide();
        $("#inputNewTodo").show().focus();
    });

    $("#inputNewTodo").blur(function() {
        $(this).hide();
        $(".search").show().focus();
    });

    $("#buttonNewTag").click(function() {
        $(".search").hide();
        $("#inputNewTodo").hide();
        $("#inputNewTag").show().focus();
    });

    $("#inputNewTag").blur(function() {
        $(this).hide();
        $(".search").show().focus();
    });



});