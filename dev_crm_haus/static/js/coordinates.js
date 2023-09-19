odoo.define("dev_crm_haus.coordinates", function (require) {
  "use strict";
  // Print out console if javascript file works
  console.log("LOADED");

  // Get Odoo View Controller and rpc
  var FormController = require("web.FormController");
  var rpc = require("web.rpc");
  // Odoo View Controller
  FormController.include({
    // Function executed on save
    _onEdit: function () {
      if (this.modelName == "crm.issue") {
        console.log("onEdit");
        var self = this;
        var sup = this._super();

        // Get Current Record
        var recordID = self.model.get(self.handle, { raw: true }).res_id;

        console.log(recordID);
        // If record obtained, browser ask user for coordinates using GPS
        if (recordID) {
          navigator.geolocation.getCurrentPosition(function (position) {
            const { latitude, longitude } = position.coords;
            const coords = {
              latitude,
              longitude,
            };
            console.log(coords);
            // Write record
            rpc
              .query({
                model: "crm.issue",
                method: "write",
                args: [
                  [recordID],
                  { latitude: coords.latitude, longitude: coords.longitude },
                ],
              })
              .then(function () {
                self.trigger_up("reload");
                rpc
                  .query({
                    model: "crm.issue",
                    method: "read",
                    args: [[recordID], ["is_near_one_km"]],
                  })
                  .then(function (result) {
                    if (result[0].is_near_one_km == false) {
                      self.displayNotification({
                        type: "warning",
                        title: "WARNING",
                        message: "Your Location is too far from office",
                        sticky: true,
                      });
                    }
                  });
              });
          });
        }
        return sup;
      }
    },
  });

  return FormController;
});
