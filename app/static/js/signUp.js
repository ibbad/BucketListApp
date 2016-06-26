$(function () {
    $('#btnSignUp').click(function () {
        console.log('Button pressed');
        $.ajax({
            url: '/signup',
            data: $('form').serialize(),
            type:'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});