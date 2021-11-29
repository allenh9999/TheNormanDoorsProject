<template>
   
   <div style="width: 90%; margin-left: auto; margin-right: auto; text-align: center">
      <div class="accordion" style="width: 50%; margin-left: auto; margin-right: auto" id="mainAccordion">
         <div class="accordion-item">
            <h2 class="accordion-header" id="addHeading">
               <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#addCollapse" aria-expanded="true" aria-controls="addCollapse" style="font-size: 0.7em">
                  Create Group
               </button>
            </h2>
            <div class="accordion-collapse collapse show" id="addCollapse" aria-labelledby="addHeading" data-bs-parent="#mainAccordion">
               <div class="accordion-body">
                  <div class="form-floating mb-3">
                     <input type="name" class="form-control" id="addName" placeholder="Name"> <!--class invalid-->
                     <label for="addName">Group Name</label>
                  </div>
                  <div class="form-floating">
                     <input type="password" class="form-control" id="addPassword" placeholder="Password">
                     <label for="addPassword">Password</label>
                  </div>
                  <div style="height: 20px"></div>
                  <button type="button" class="btn btn-outline-primary" style="width: 200px; font-size: 1.4em" @click="addGroup()">Create</button>
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
               $(addPassword)[0].value = "";
               $(addPassword).addClass("is-invalid");
               if (data.data == "name") {
                  $(addName)[0].value = "";
                  $(addName).addClass("is-invalid");
               }
            } else {
               window.location.href = "/feed/";
            }
         });
      }
   }
};
</script>