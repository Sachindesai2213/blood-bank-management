const donationRequestGrid = (donation_requests) => {
    $('#donation-request-grid').dxDataGrid({
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
                dataField: "requirement__user__first_name",
                caption: "Raised By",
            },
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
                dataField: "acceptance_status",
                caption: "Acceptance Status",
            },
        ],
        showBorders: true,
    })
}