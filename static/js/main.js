$(function () {
    var message = $('.js-alert');
    var form = $('.js-record-form');

    form.on('submit',function () {
        $.post($(this).attr('action'),$(this).serialize(),function (result) {
            message.removeClass('alert-success');
            message.removeClass('alert-danger');

            $('.form-group').removeClass('has-error');
            $('.form-group .help-block').html('');

            if(result.RESULT)
                message.addClass('alert-success')
            else
                message.addClass('alert-danger')

            for (var key in result.DATA){
                if ($('.js-form-'+key).length>0){
                    $('.js-form-'+key).addClass('has-error');
                    $('.js-form-'+key).find('.help-block').html(result.DATA[key]);
                }
            }

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
