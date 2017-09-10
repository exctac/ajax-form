$(document).ready(function () {
    $('input[data-inputmask]').inputmask();
    $('form').ajaxForm({
        dataType:  'json',
        type: 'post',
        success: function(responseText, statusText, xhr, $form) {
            if (responseText['result'] == 'success') {
                $form.prev('.alert').remove()
                $form.find('.invalid-feedback').remove()
                $form
                    .before(
                        '<div class="alert alert-success" role="alert">' +
                            '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                                '<span aria-hidden="true">&times;</span>' +
                            '</button>' + responseText['response'] +
                        '</div>')
                    .find('.form-group input').removeClass('is-invalid').val('')
            }
            else if (responseText['result'] == 'error') {
                $form.find('.invalid-feedback').remove()
                $form.prev('.alert').remove()
                $form.find('input').removeClass('is-invalid')
                for (var k in responseText['response']) {
                    $form
                        .find('input[name=' + k + ']')
                        .addClass('is-invalid')
                        .parents('.input-group')
                        .after('<div class="invalid-feedback d-block text-right">' + responseText['response'][k][k] + '</div>');
                }
            }
        },
        error: function(xhr, statusText, error , $form) {}
    })
})