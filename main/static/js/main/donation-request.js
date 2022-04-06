const acceptDonationRequest = (donation_request_id) => {
    $('#raise-'+donation_request_id).attr('disabled', true);
    $('#raise-'+donation_request_id).html('Accepting<i class="fa fa-spinner fa-spin"></i>');
    $.ajax({
        url: '/api/requirement-donor/'+donation_request_id+'/',
        type: 'PATCH',
        headers: {
            'X-CSRFToken': csrftoken,
        },
        success: function (data) {
            $('#raise-'+donation_request_id).attr('disabled', false);
            $('#raise-'+donation_request_id).html('Accept');
            // if (data.status == "success") {
            //     $("#donation-requests-grid").dxDataGrid("instance").refresh();
            // }
        },
        error: function (data) {
            $('#raise-'+donation_request_id).attr('disabled', false);
            $('#raise-'+donation_request_id).html('Accept');
            console.log("data", data);
        }
    })
}

const donationRequestsGrid = (donation_requests) => {
    $('#donation-requests-grid').dxDataGrid({
        dataSource: donation_requests,
        dataSource: donation_requests,
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
                dataField: "requirement__location",
                caption: "Location",
            },
            {
                dataField: "requirement__blood_type__abbr",
                caption: "Blood Type",
            },
            {
                dataField: "requirement__description",
                caption: "Description",
            },
            {
                dataField: "requirement__quantity",
                caption: "Quantity",
            },
            {
                dataField: "requirement__requirement_fulfilled",
                caption: "Requirement Fulfilled",
            },
            {
                dataField: "requirement__date_time",
                caption: "Raised on",
            },
            {
                dataField: "donor__first_name",
                caption: "Donor",
            },
            {
                dataField: "acceptance_status",
                caption: "Acceptance Status",
            },
            {
                caption: "Accept Donation Request",
                cellTemplate: function (container, options) {
                    rowData = options.data;
                    console.log("rowData", rowData);
                    container.append('<button class="m-0 btn btn-sm btn-primary" id="raise-'+rowData.id+'" onClick="acceptDonationRequest('+rowData.id+')">Accept</button>')
                }
            },
        ],
        showBorders: true,
    });
}