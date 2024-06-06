
const placeMarkers = new Map();

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 20, lng: 0},
        zoom: 2,
        mapId: "ed98efda5614b742"
    });
    var input = document.createElement('input');
    input.id = 'map-search-box';
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

    var autocomplete = new google.maps.places.Autocomplete(input);
    autocomplete.bindTo('bounds', map);
    
    
    var marker;  // Marker initialization

    autocomplete.addListener('place_changed', function() {
        var place = autocomplete.getPlace();
        if (!place.geometry) {
            console.log("No details available for input: '" + place.name + "'");
            return;
        }

        if (place.geometry.viewport) {
            map.fitBounds(place.geometry.viewport);
        } else {
            map.setCenter(place.geometry.location);
            map.setZoom(17);
        }

        if (marker) {  // Check if marker already exists
            marker.setMap(null);  // Remove the existing marker
        }
        marker = new google.maps.Marker({
            map: map,
            position: place.geometry.location
        });

        displayPlaceDetails(place, map);  // Display details in the dedicated div
    });
}

function displayPlaceDetails(place, map) {
    var placeInfoDiv = document.getElementById('place-info');
    placeInfoDiv.innerHTML = "";
    var card = document.createElement('div');
    card.className = "card";
    var content = '';

    if (place.photos && place.photos.length > 0) {
        var photoUrl = place.photos[0].getUrl({ maxWidth: 400, maxHeight: 300 });
        content += '<img src="' + photoUrl + '" alt="' + place.name + ' photo" class="card-img-top">';
    }
    content += '<div class="card-body"><h5 class="card-title">' + place.name + '</h5>';

    content += '<p><strong>Address:</strong> ' + (place.formatted_address || 'No address available') + '</p>';

    if (place.international_phone_number) {
        content += '<p><strong>Phone Number:</strong> ' + place.international_phone_number + '</p>';
    }
    if (place.rating) {
        content += '<p><strong>Rating:</strong> ' + place.rating + ' / 5</p>';
    }
    if (place.website) {
        content += '<p><strong>Website:</strong> <a href="' + place.website + '" target="_blank">' + place.website + '</a></p>';
    }
    content += '<button class="btn btn-info add-place-button">Add this place</button>';
    card.innerHTML = content;
    placeInfoDiv.appendChild(card);

    // Set up the add button event listener
    card.querySelector('.add-place-button').addEventListener('click', function() {
        addPlace(place, map);  // Function to handle place saving or further actions
        console.log(place.name);
        placeInfoDiv.removeChild(card);


    });
}



function addPlace(place, map) {
    console.log("Place added: ", place.name);  // Implement functionality as needed

    var customIcon = {
        url: 'images/flag.png',  // URL of the image
        scaledSize: new google.maps.Size(40, 40),  // Size in pixels
        origin: new google.maps.Point(0, 0),  // Position at the top-left corner of the image
        anchor: new google.maps.Point(20, 40)  // Anchor at the bottom-center of the icon
    };

    customIcon = 'images/flag.png';

    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location
        //icon: customIcon
    });
    placeMarkers.set(place.name, marker);
    var placeListDiv = document.getElementById('place-list');
    var card2 = document.createElement("div");
    card2.className = "card w-50 single-place-card";
    var content2 = '<div class="card-body"><h5 class="card-title">'+ place.name + '</h5><input type="text" style="width: 30px;"><span> hours </span><a style="margin-left:130px;" href="#" class="btn btn-info remove-place-button">X</a></div>';
    card2.innerHTML = content2;
    placeListDiv.appendChild(card2);

    card2.querySelector('.remove-place-button').addEventListener('click', function() {
        removePlace(card2, place.name);
    });
}

function removePlace(card, placeName){
    card.parentNode.removeChild(card);
    const marker = placeMarkers.get(placeName);
    if (marker) {
        marker.setMap(null);  // Removes the marker from the map
        placeMarkers.delete(placeName);  // Removes the reference from the map
    }
}
            
