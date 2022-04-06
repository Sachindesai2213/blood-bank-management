const requirementsGrid = (requirements) => {
    $("#requirements-grid").dxDataGrid({
        dataSource: requirements,
        // editing: {
        //     mode: "row",
        //     allowUpdating: true,
        //     allowDeleting: true,
        //     allowAdding: true
        // },
        headerFilter: {
            visible: true
        },
        filterRow: { visible: true },
        paging: {
            enabled: false,
        },
        showPane: false,
        columns: [
            {
                dataField: "blood_type__abbr",
                caption: "Blood Type",
            },
            {
                dataField: "location",
                caption: "Location",
            },
            {
                dataField: "description",
                caption: "Description",
            },
            {
                dataField: "quantity",
                caption: "Quantity",
            },
            {
                dataField: "requirement_fulfilled",
                caption: "Requirement Fulfilled",
            },
            {
                dataField: "date_time",
                caption: "Raised on",
            }
        ],
        showBorders: true,
    });
};

$('#add-requirement-form').submit((event) => {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/requirements/',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            blood_type_id: $('#blood-group').val(),
            quantity: $('#quantity').val(),
            location: $('#location').val(),
            description: $('#description').val(),
        },
        success: (data) => {
            console.log(data);
            $('#requirements-grid').dxDataGrid({
                dataSource: data.user_requirements,
            });
            $('#exampleModal').modal('hide');
        },
        error: (err) => {
            alert('error while creating requirement');
            $('#exampleModal').modal('hide');
        }
    });
})