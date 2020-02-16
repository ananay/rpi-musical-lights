$(document).ready(() => {
    $(".box").click((e) => {
        $(".box").removeClass('active');
        $(e.target).addClass('active');
    });

    $("#spectrum").click(() => {
        $.get('/spectrum', (r) => {
            console.log(r);
        });
    });

});