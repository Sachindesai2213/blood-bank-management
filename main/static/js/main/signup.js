$('#signup-form').submit(event => {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/signup/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            username: $('#username').val(),
            first_name: $('#first-name').val(),
            last_name: $('#last-name').val(),
            email: $('#email').val(),
            age: $('#age').val(),
            password: $('#password').val(),
            blood_group: $('#blood-group').val(),
            contact: $('#contact').val(),
        },
        success: (data) => {
            console.log(data);
            window.location.href = '/login/';
        },
        error: (err) => {
            console.log(err);
        }
    });
})