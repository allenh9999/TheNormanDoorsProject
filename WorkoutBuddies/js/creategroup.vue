<template>
   
   <div style="width: 90%; margin-left: auto; margin-right: auto; text-align: center">
      <div class="accordion" style="width: 50%; margin-left: auto; margin-right: auto" id="mainAccordion">
         <div class="accordion-item">
            <h2 class="accordion-header" id="createHeading">
               <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#createCollapse" aria-expanded="true" aria-controls="createCollapse" style="font-size: 0.7em">
                  Create Group
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
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
      };
   },
   methods: {
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
               $(createPassword)[0].value = "";
               $(createPassword).addClass("is-invalid");
               if (data.data == "name") {
                  $(createName)[0].value = "";
                  $(createName).addClass("is-invalid");
               }
            } else {
               window.location.href = "/feed/";
            }
         });
      }
   }
};
</script>