
$("#data tr").click(function() {
    var selected = $(this).hasClass("highlight");
    $("#data tr").removeClass("highlight");
    if(!selected)
            $(this).addClass("highlight");
});