<template>
   
   <div style="width: 90%; margin-left: auto; margin-right: auto; text-align: center">
      <div style="height: 20px"></div>
      <div class="accordion" style="width: 50%; margin-left: auto; margin-right: auto" id="mainAccordion">
         <div class="accordion-item">
            <h2 class="accordion-header" id="createHeading">
               <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#createCollapse" aria-expanded="true" aria-controls="createCollapse" style="font-size: 0.7em">
                  Create a group!
               </button>
            </h2>
            <div class="accordion-collapse collapse show" id="createCollapse" aria-labelledby="logInHeading" data-bs-parent="#mainAccordion">
               <div class="accordion-body">
                  <div class="form-floating mb-3">
                     <input type="name" class="form-control" id="createName" placeholder="Name"> <!--class invalid-->
                     <label for="createName">Group Name</label>
                  </div>
                  <div class="form-floating">
                     <input type="password" class="form-control" id="createPassword" placeholder="Password">
                     <label for="createPassword">Password</label>
                  </div>
                  <div style="height: 20px"></div>
                  <button type="button" class="btn btn-outline-primary" style="width: 200px; font-size: 1.4em" @click="create()">Create</button>
               </div>
            </div>
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
      create() {
         $(createName).removeClass("is-invalid");
         $(createPassword).removeClass("is-invalid");
         let sendData = {
            name: $(createName)[0].value,
            password: $(createPassword)[0].value,
         };
         fetch("/api/create/", { method: "POST", credentials: 'same-origin', body: JSON.stringify(sendData) })
         .then((response) => {
           if (!response.ok) throw Error(response.statusText);
           return response.json();
         })
         .then((data) => {
            if (data.status == "failed") {
               if (data.data == "name") {
                  $(createName).addClass("is-invalid");
                  this.send_error("The name needs to be longer");
               } else if (data.data == "password") {
                  this.send_error("The password needs to be longer");
                  $(createPassword)[0].value = "";
                  $(createPassword).addClass("is-invalid");
               } else {
                  $(createName).addClass("is-invalid");
                  this.send_error("There is already a group named " + $(createName)[0].value);
               }
            } else {
               window.location.href = "/feed/";
            }
         });
      }
   }
};
</script>