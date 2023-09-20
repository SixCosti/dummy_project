document.addEventListener("DOMContentLoaded", () => {
    // Fetch licenses from your Django API here using the correct serializer

    const licenseList = document.getElementById("license-list");

    fetch("/api/licenses/") // Replace with your actual API endpoint
        .then((response) => response.json())
        .then((data) => {
            data.forEach((license) => {
                const listItem = document.createElement("li");
                listItem.innerHTML = `<strong>${license.name}</strong> - Total: ${license.total_licenses}, In Use: ${license.licenses_in_use}, Expires on: ${license.expiry_date}`;
                licenseList.appendChild(listItem);
            });
        })
        .catch((error) => console.error("Error fetching licenses:", error));

    // Similar code can be used to fetch and display users
});
