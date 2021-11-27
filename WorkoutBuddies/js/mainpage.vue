<template>
   
   <div style="width: 90%; margin-left: auto; margin-right: auto; text-align: center">
      <h1 style="text-decoration: underline; text-decoration-color: blue; font-size: 4em;">Welcome to Workout Buddies!</h1>
      <p style="font-size: 1.5em">This is an area for people to post their workouts, and this community focuses on motivation and engagement.</p>
      <div class="accordion" style="width: 50%; margin-left: auto; margin-right: auto" id="mainAccordion">
         <div class="accordion-item">
            <h2 class="accordion-header" id="logInHeading">
               <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#logInCollapse" aria-expanded="true" aria-controls="logInCollapse" style="font-size: 0.7em">
                  Log in
               </button>
            </h2>
            <div class="accordion-collapse collapse show" id="logInCollapse" aria-labelledby="logInHeading" data-bs-parent="#mainAccordion">
               <div class="accordion-body">
                  <p>To do</p>
               </div>
            </div>
         </div>
         <div class="accordion-item">
            <h2 class="accordion-header" id="signUpHeading">
               <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#signUpCollapse" aria-expanded="false" aria-controls="signUpCollapse" style="font-size: 0.7em">
                  Sign up
               </button>
            </h2>
            <div class="accordion-collapse collapse" id="signUpCollapse" aria-labelledby="signUpHeading" data-bs-parent="#mainAccordion">
               <div class="accordion-body">
                  <p>To do</p>
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
};
</script>