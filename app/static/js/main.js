document.addEventListener('DOMContentLoaded', function() {
    // Use My Location button click handler
    document.getElementById('use-location-btn').addEventListener('click', function() {
        if ('geolocation' in navigator) {
            navigator.geolocation.getCurrentPosition(function(position) {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                const locationInput = document.getElementById('location-input');
                locationInput.value = latitude + ',' + longitude;
            });
        } else {
            alert('Geolocation is not supported by this browser.');
        }
    });
});
