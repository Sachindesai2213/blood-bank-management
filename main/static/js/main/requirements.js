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

const raiseDonationRequest = (requirement_id) => {
    $('#raise-'+requirement_id).attr('disabled', true);
    $('#raise-'+requirement_id).html('Raising<i class="fa fa-spinner fa-spin"></i>');
    console.log(requirement_id)
    $.ajax({
        url: '/api/requirement-donors/',
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        data: {
            'requirement_id': requirement_id,
        },
        success: function (data) {
            $('#raise-'+requirement_id).attr('disabled', false);
            $('#raise-'+requirement_id).html('Raise');
            // if (data.status == "success") {
            //     $("#requirements-grid").dxDataGrid("instance").refresh();
            //     $("#global-requirements-grid").dxDataGrid("instance").refresh();
            // }
        },
        error: function (data) {
            $('#raise-'+requirement_id).attr('disabled', false);
            $('#raise-'+requirement_id).html('Raise');
            console.log("data", data);
        }
    })
}

const globalRequirementsGrid = (requirements) => {
    $("#global-requirements-grid").dxDataGrid({
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
            },
            {
                dataField: "donation_request",
                caption: "Raise Donation",
                cellTemplate: function (container, options) {
                    rowData = options.data;
                    console.log("rowData", rowData);
                    container.append('<button class="m-0 btn btn-sm btn-primary" id="raise-'+rowData.id+'" onClick="raiseDonationRequest('+rowData.id+')">Raise</button>')
                }
            },
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