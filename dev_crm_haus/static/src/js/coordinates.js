odoo.define("dev_crm_haus.coordinates", function (require) {
  navigator.geolocation.getCurrentPosition(
    successCallback,
    errorCallback,
    options
  );

  function successCallback(position) {
    const { accuracy, latitude, longitude, altitude, heading, speed } =
      position.coords;
    fieldValues = {
      latitude: latitude,
      longitude: longitude,
    };
    document.getElementById("o_field_input_13").value = latitude;
    document.getElementById("o_field_input_14").value = longitude;

    console.log(latitude, longitude);
  }
  function errorCallback(error) {}
  var options = {};
});
