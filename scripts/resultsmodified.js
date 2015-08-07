//
// service = new google.maps.places.PlacesService(map);
// service.nearbySearch(request, callback);

$(document).ready( function() {
  console.log("HEY");
  initialize();
});


// ------------------------------------------

var map;
var infowindow;
var service;
var directionsDisplay = new google.maps.DirectionsRenderer();
var directionsService = new google.maps.DirectionsService();

function initialize() {

  console.log("ohhh");
  maps-canvas = new google.maps.Map(document.getElementById('maps-canvas'), {
                            center: {lat: 44, lng: 100},
                            zoom: 15
                          });
  directionsDisplay.setMap(maps-canvas);
  service = new google.maps.places.PlacesService(maps-canvas);
  infoWindow = new google.maps.InfoWindow();
  testFunction();
}

function testFunction() {
    var start = new google.maps.LatLng(41.90742500122083,-87.67729600470253);
    var end = new google.maps.LatLng(44.1, -90.5);

    console.log("MARKER1");
    var marker1 = new google.maps.Marker({
      map: maps-canvas,
      position: start
    });
    console.log("MARKER2");

    var marker2 = new google.maps.Marker({
      map: maps-canvas,
      position: end
    });
    console.log("SET CENTER");
    map.setCenter(marker1.position);
    map.setZoom(8);
    var request = {
    origin:start,
    destination: end,
    travelMode: google.maps.TravelMode.DRIVING
  };
  directionsService.route(request, function(result, status) {
    console.log(result);
    console.log(status);
    if (status == google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(result);
    }
  });
}


function createMarker(place) {


  google.maps.event.addListener(marker, 'click', function() {
    service.getDetails(place, function(result, status) {
      if (status != google.maps.places.PlacesServiceStatus.OK) {
        alert(status);
        return;
      }
      infoWindow.setContent(result.name);
      infoWindow.open(maps-canvas, marker);
    });
  });
}

// function initialize() {
//     var myLatlng = new google.maps.LatLng( 41.907,-87.67729600470253);
//     var mapOptions = {
//       zoom: 12,
//       center: myLatlng
//     }
//     var map = new google.maps.Map(document.getElementById('maps-canvas'), mapOptions);
//
//     var marker1 = new google.maps.Marker({
//         position: new google.maps.LatLng( 41.90742500122083,-87.67729600470253),
//         map: map,
//         label: "Ellis",
//       });
//
//
//       marker1.setMap(map);
//     google.maps.event.addDomListener(window, 'load', initialize);
//
//     if(navigator.geolocation) {
//     navigator.geolocation.getCurrentPosition(function(position) {
//       var pos = new google.maps.LatLng(position.coords.latitude,
//                                        position.coords.longitude);
//
//       var infowindow = new google.maps.InfoWindow({
//         map: map,
//         position: pos,
//         content: 'Location found using HTML5.'
//       });
//
//       map.setCenter(pos);
//     }, function() {
//       handleNoGeolocation(true);
//     });
//   } else {
//     // Browser doesn't support Geolocation
//     handleNoGeolocation(false);
//   }
// }

function handleNoGeolocation(errorFlag) {
  if (errorFlag) {
    var content = 'Error: The Geolocation service failed.';
  } else {
    var content = 'Error: Your browser doesn\'t support geolocation.';
  }

  var options = {
    map: maps-canvas,
    position: new google.maps.LatLng(60, 105),
    content: content
  };

  var infowindow = new google.maps.InfoWindow(options);
  map.setCenter(options.position);
}

// google.maps.event.addDomListener(window, 'load', initialize);


  google.maps.event.addDomListener(window, 'load', initialize);

  $('#back_button').click(function(){
      parent.history.back();
      return false;
    });

//
//
//   function callback(results, status) {
//     if (status == google.maps.places.PlacesServiceStatus.OK) {
//       for (var i = 0; i < results.length; i++) {
//         var place = results[i];
//         createMarker(results[i]);
//       }
//     }
//   }
//
// service = new google.maps.places.PlacesService(map);
// service.radarSearch(request, callback);
//
// var map;
// var infoWindow;
// var service;
//
// map = new google.maps.Map(document.getElementById('map-canvas'), {
//   center: new google.maps.LatLng(-33.8668283734, 151.2064891821),
//   zoom: 15,
//   styles: [
//       {
//         stylers: [
//           { visibility: 'simplified' }
//         ]
//       },
//       {
//         elementType: 'labels',
//         stylers: [
//           { visibility: 'off' }
//         ]
//       }
//     ]
//   })
//
//
//   service = new google.maps.places.PlacesService(map);
//
//   google.maps.event.addListenerOnce(map, 'bounds_changed', performSearch);
// }
//
// function performSearch() {
//   var request = {
//     bounds: map.getBounds(),
//     keyword: 'best view'
//   };
//   service.radarSearch(request, callback);
// }
//
// function callback(results, status) {
//   if (status != google.maps.places.PlacesServiceStatus.OK) {
//     alert(status);
//     return;
//   }
//   for (var i = 0, result; result = results[i]; i++) {
//     createMarker(result);
//   }
// }
//

//

//
// google.maps.event.addDomListener(window, 'load', initialize);
//
// var map, placesList;
//
// function initialize() {
//   var pyrmont = new google.maps.LatLng(-33.8665433, 151.1956316);
//
//   map = new google.maps.Map(document.getElementById('map-canvas'), {
//     center: pyrmont,
//     zoom: 17
//   });
//
//   var request = {
//     location: pyrmont,
//     radius: 500,
//     types: ['store']
//   };
//
//   placesList = document.getElementById('places');
//
//   var service = new google.maps.places.PlacesService(map);
//   service.nearbySearch(request, callback);
// }
//
// function callback(results, status, pagination) {
//   if (status != google.maps.places.PlacesServiceStatus.OK) {
//     return;
//   } else {
//     createMarkers(results);
//
//     if (pagination.hasNextPage) {
//       var moreButton = document.getElementById('more');
//
//       moreButton.disabled = false;
//
//       google.maps.event.addDomListenerOnce(moreButton, 'click',
//           function() {
//         moreButton.disabled = true;
//         pagination.nextPage();
//       });
//     }
//   }
// }
//
// function createMarkers(places) {
//   var bounds = new google.maps.LatLngBounds();
//
//   for (var i = 0, place; place = places[i]; i++) {
//     var image = {
//       url: place.icon,
//       size: new google.maps.Size(71, 71),
//       origin: new google.maps.Point(0, 0),
//       anchor: new google.maps.Point(17, 34),
//       scaledSize: new google.maps.Size(25, 25)
//     };
//
//     var marker = new google.maps.Marker({
//       map: map,
//       icon: image,
//       title: place.name,
//       position: place.geometry.location
//     });
//
//     placesList.innerHTML += '<li>' + place.name + '</li>';
//
//     bounds.extend(place.geometry.location);
//   }
//   map.fitBounds(bounds);
// }
//
// google.maps.event.addDomListener(window, 'load', initialize);
//
// service = new google.maps.places.PlacesService(map);
// service.getDetails(request, callback);
//
// var request = {
//   placeId: 'ChIJN1t_tDeuEmsRUsoyG83frY4'
// };
//
// service = new google.maps.places.PlacesService(map);
// service.getDetails(request, callback);
//
// function callback(place, status) {
//   if (status == google.maps.places.PlacesServiceStatus.OK) {
//     createMarker(place);
//   }
// }
//
// var map;
//
// function initialize() {
//   // Create a map centered in Pyrmont, Sydney (Australia).
//   map = new google.maps.Map(document.getElementById('map-canvas'), {
//     center: {lat: -33.8666, lng: 151.1958},
//     zoom: 15
//   });
//
//   // Search for Google's office in Australia.
//   var request = {
//     location: map.getCenter(),
//     radius: '500',
//     query: 'Google Sydney'
//   };
//
//   var service = new google.maps.places.PlacesService(map);
//   service.textSearch(request, callback);
// }
//
// // Checks that the PlacesServiceStatus is OK, and adds a marker
// // using the place ID and location from the PlacesService.
// function callback(results, status) {
//   if (status == google.maps.places.PlacesServiceStatus.OK) {
//     var marker = new google.maps.Marker({
//       map: map,
//       place: {
//         placeId: results[0].place_id,
//         location: results[0].geometry.location
//       }
//     });
//   }
// }
//
// function createPhotoMarker(place) {
//   var photos = place.photos;
//   if (!photos) {
//     return;
//   }
// }
//   var marker = new google.maps.Marker({
//     map: map,
//     position: place.geometry.location,
//     title: place.name,
//     icon: photos[0].getUrl({'maxWidth': 35, 'maxHeight': 35})
//   })
