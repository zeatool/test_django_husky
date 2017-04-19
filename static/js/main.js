$(function () {
    var message = $('.js-alert');
    var form = $('.js-record-form');

    form.on('submit',function () {
        $.post($(this).attr('action'),$(this).serialize(),function (result) {
            message.removeClass('alert-success');
            message.removeClass('alert-danger');

            if(result.RESULT)
                message.addClass('alert-success')
            else
                message.addClass('alert-danger')

            message.html(result.MESSAGE)
        },'json')

       return false;
    })

    $('.js-date').datepicker({
         language: "ru",
         orientation: "bottom auto",
         autoclose: true
    });
})
