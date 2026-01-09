function filterItems() {
    let searchQuery = document.getElementById("search-box").value.toLowerCase();
    let rows = document.querySelectorAll("#items-container tbody tr");

    rows.forEach(row => {
        let input = row.querySelector("input.product-checkbox");
        if (input) {
            let name = input.getAttribute("data-nombre") ? input.getAttribute("data-nombre").toLowerCase() : "";
            if (name.includes(searchQuery)) {
                row.style.display = "table-row";
            } else {
                row.style.display = "none";
            }
        }
    });
}