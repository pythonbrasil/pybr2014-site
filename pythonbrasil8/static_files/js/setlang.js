$(document).ready(function() {
    $(".btn-setlang").click(function(e) {
        var form = $(this).parent();
        form.find("input[name='language']").val(
            $(this).attr("data-language")
        );
        form.submit();
    });
});