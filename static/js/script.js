/* Confirmation prompt upon deleting a post */
function confirmDelete() {
    if (confirm('Are you sure you want to delete your post?')) {
        document.getElementById('deleteForm').submit();
    }
}