//delete confirmation alert 


function confirmDelete() {
    if (confirm('Are you sure you want to delete this item?')) {
        // If the user confirms, the form will be submitted as usual.
        return true;
    } else {
        // If the user cancels, the form submission is canceled.
        return false;
    }
}