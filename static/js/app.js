$(document).ready(() => {
    $(".box").click((e) => {
        $(".box").removeClass('active');
        $(e.target).addClass('active');
    });

    $.get('/status', (r) => {
        $(".box").removeClass('active');
        $('#' + r).addClass('active');
    })

    $("#spectrum").click(() => {
        $.get('/spectrum', (r) => {
            $(".box").removeClass('active');
            $("#spectrum").addClass('active');
        });
    });

    $("#scroll").click(() => {
        $.get('/scroll', (r) => {
            $(".box").removeClass('active');
            $("#scroll").addClass('active');
        });
    });

    $("#energy").click(() => {
        $.get('/energy', (r) => {
            $(".box").removeClass('active');
            $("#energy").addClass('active');
        });
    });

    $("#off").click(() => {
        $.get('/kill', (r) => {
            $(".box").removeClass('active');
            $("#off").addClass('active');
        });
    });

});