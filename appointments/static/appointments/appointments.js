document.addEventListener('DOMContentLoaded', function() {
    // Add event listeners to each sort button after the DOM is fully loaded
    document.querySelectorAll('.sort-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();  // Prevent the default link behavior
            const column = this.getAttribute('data-column'); // Get the column to sort by
            sortTable(column); // Call the sorting function
        });
    });
});

function sortTable(column) {
    const table = document.querySelector('table'); // Get the table
    const tbody = table.querySelector('tbody'); // Get the tbody
    const rows = Array.from(tbody.querySelectorAll('tr')); // Get all rows except the header

    const getCellText = (row, index) => row.cells[index]?.textContent.trim() || '';

    const columnIndex = {
        'professor': 0,   // Professor is in the first column
        'student': 0,     // Student is in the first column for professor role
        'date': 1,        // Date is in the second column
        'reason': 2,      // Reason is in the third column
        'status': 3       // Status is in the fourth column
    };

    // Sort rows based on the selected column
    const sortedRows = rows.sort((a, b) => {
        const cellA = getCellText(a, columnIndex[column]);
        const cellB = getCellText(b, columnIndex[column]);

        if (column === 'date') {
            // Convert the date text to a proper Date object
            const dateA = new Date(cellA);
            const dateB = new Date(cellB);

            if (isNaN(dateA) || isNaN(dateB)) {
                // In case date parsing fails, keep as it is (handle any parsing errors)
                return 0;
            }

            return dateA - dateB; // Compare dates
        } else {
            return cellA.localeCompare(cellB); // For text-based columns like professor, reason, status
        }
    });

    // Re-insert sorted rows back into the table body
    sortedRows.forEach(row => tbody.appendChild(row));
}