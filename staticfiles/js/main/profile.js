$('#profile-form').submit(event => {
    event.preventDefault();
    $.ajax({
        type: 'PUT',
        url: '/api/signup/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            first_name: $('#first-name').val(),
            last_name: $('#last-name').val(),
            contact: $('#contact').val(),
            blood_type_id: $('#blood-group').val(),
            email: $('#email').val(),
        },
        success: (data) => {
        },
        error: (err) => {
            console.log(err);
        }
    });
})