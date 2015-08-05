
$(document).ready(function() {
  function initialize() {    var myLatlng = new google.maps.LatLng( 41.907,-87.67729600470253);    var mapOptions = {      zoom: 12,      center: myLatlng    }    var map = new google.maps.Map(document.getElementById('maps-canvas'), mapOptions);    var marker1 = new google.maps.Marker({        position: new google.maps.LatLng( 41.90742500122083,-87.67729600470253),        map: map,    });    if(navigator.geolocation) {    navigator.geolocation.getCurrentPosition(function(position) {      var pos = new google.maps.LatLng(position.coords.latitude,                                       position.coords.longitude);      var infowindow = new google.maps.InfoWindow({        map: map,        position: pos,        content: 'Location found using HTML5.'      });      map.setCenter(pos);    }, function() {      handleNoGeolocation(true);    });  } else {    // Browser doesn't support Geolocation    handleNoGeolocation(false);  }}function handleNoGeolocation(errorFlag) {  if (errorFlag) {    var content = 'Error: The Geolocation service failed.';  } else {    var content = 'Error: Your browser doesn\'t support geolocation.';  }  var options = {    map: map,    position: new google.maps.LatLng(60, 105),    content: content  };  var infowindow = new google.maps.InfoWindow(options);  map.setCenter(options.position);}google.maps.event.addDomListener(window, 'load', initialize);  })  google.maps.event.addDomListener(window, 'load', initialize);  $('#back_button').click(function(){      parent.history.back();      return false;    });