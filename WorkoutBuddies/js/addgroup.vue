<template>
   
   <div style="width: 90%; margin-left: auto; margin-right: auto; text-align: center">
      <div style="height: 20px"></div>
      <div class="card" style="width: 50%; margin-left: auto; margin-right: auto" id="mainAccordion">
         <h2 class="card-header">
            <h2>Add Group</h2>
         </h2>
         <div class="card-body">
            <div class="form-floating mb-3">
               <input type="name" class="form-control" id="addName" placeholder="Name"> <!--class invalid-->
               <label for="addName">Group Name</label>
            </div>
            <div class="form-floating">
               <input type="password" class="form-control" id="addPassword" placeholder="Password">
               <label for="addPassword">Password</label>
            </div>
            <div style="height: 20px"></div>
            <button type="button" class="btn btn-outline-primary" style="width: 200px; font-size: 1.4em" @click="addGroup()">Add!</button>
         </div>
      </div>
      <div v-if="is_error" class="alert alert-danger" style="width: 300px; position: fixed; bottom: 0px; margin-left: 45%; transform: translate(-150px, 0px); text-align: center">
         {{error_message}}
      </div>
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
         is_error: false,
         error_message: "",
         error_timeout: null,
      };
   },
   methods: {
      send_error(message) {
         clearTimeout(this.error_timeout);
         this.error_message = message;
         this.is_error = true;
         this.error_timeout = setTimeout(() => this.is_error = false, 6000);
      },
      addGroup() {
         $(addName).removeClass("is-invalid");
         $(addPassword).removeClass("is-invalid");
         let sendData = {
            name: $(addName)[0].value,
            password: $(addPassword)[0].value,
         };
         fetch("/api/addgroup/", { method: "POST", credentials: 'same-origin', body: JSON.stringify(sendData) })
         .then((response) => {
           if (!response.ok) throw Error(response.statusText);
           return response.json();
         })
         .then((data) => {
            if (data.status == "failed") {
               if (data.data == "name") {
                  $(addName).addClass("is-invalid");
                  this.send_error("No group is named " + $(addName)[0].value);
                  $(addPassword)[0].value = "";
                  $(addPassword).addClass("is-invalid");
               } else if (data.data == "password") {
                  this.send_error("The password is incorrect");
                  $(addPassword)[0].value = "";
                  $(addPassword).addClass("is-invalid");
               } else {
                  $(addName).addClass("is-invalid");
                  this.send_error("You already are in this group");
               }
            } else {
               window.location.href = "/feed/";
            }
         });
      }
   }
};
</script>