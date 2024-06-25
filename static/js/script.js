// Confirmation prompt upon deleting a post 
function confirmDelete() {
    if (confirm('Are you sure you want to delete your post?')) {
        document.getElementById('deleteForm').submit();
    }
}

// Search bar toggle small devices 
document.addEventListener("DOMContentLoaded", function () {
    const searchIcon = document.getElementById("searchIcon");
    const searchFormContainer = document.getElementById("searchFormContainer");

    searchIcon.addEventListener("click", function () {
        searchFormContainer.classList.toggle("show");
        if (searchFormContainer.classList.contains("show")) {
            searchIcon.style.display = "none";
        } else {
            searchIcon.style.display = "block";
        }
    });
});