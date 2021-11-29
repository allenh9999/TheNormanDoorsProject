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
                  <div class="form-floating mb-3">
                     <input type="email" class="form-control" id="logInEmail" placeholder="name@email.com"> <!--class invalid-->
                     <label for="logInEmail">Email address/Username</label>
                  </div>
                  <div class="form-floating">
                     <input type="password" class="form-control" id="logInPassword" placeholder="Password">
                     <label for="logInPassword">Password</label>
                  </div>
                  <div style="height: 20px"></div>
                  <button type="button" class="btn btn-outline-primary" style="width: 200px; font-size: 1.4em" @click="login()">Log in</button>
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
                  <div class="form-floating mb-3">
                     <input type="text" class="form-control" id="signUpUsername" placeholder="hello">
                     <label for="signUpUsername">Username</label>
                  </div>
                  <div class="form-floating mb-3">
                     <input type="text" class="form-control" id="signUpFirstname" placeholder="First name">
                     <label for="signUpFirstname">First name</label>
                  </div>
                  <div class="form-floating mb-3">
                     <input type="text" class="form-control" id="signUpLastname" placeholder="Last name">
                     <label for="signUpLastname">Last name</label>
                  </div>
                  <div class="form-floating mb-3">
                     <input type="number" class="form-control" id="signUpWeight" placeholder="Weight">
                     <label for="signUpWeight">weight (lbs)</label>
                  </div>
                  <div class="form-floating mb-3">
                     <input type="email" class="form-control" id="signUpEmail" placeholder="Email">
                     <label for="signUpEmail">Email</label>
                  </div>
                  <div class="form-floating mb-3">
                     <input type="password" class="form-control" id="signUpPassword" placeholder="Password">
                     <label for="signUpPassword">Password</label>
                  </div>
                  <div class="form-floating mb-3">
                     <input type="password" class="form-control" id="signUpPasswordConfirm" placeholder="Password">
                     <label for="signUpPasswordConfirm">Confirm password</label>
                  </div>
                  <button type="button" class="btn btn-outline-primary" style="width: 200px; font-size: 1.4em" @click="signup()">Sign up</button>
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
      login() {
         $(logInEmail).removeClass("is-invalid");
         $(logInPassword).removeClass("is-invalid");
         let sendData = {
            username: $(logInEmail)[0].value,
            password: $(logInPassword)[0].value,
         };
         fetch("/api/login/", { method: "POST", credentials: 'same-origin', body: JSON.stringify(sendData) })
         .then((response) => {
           if (!response.ok) throw Error(response.statusText);
           return response.json();
         })
         .then((data) => {
            if (data.status == "failed") {
               $(logInPassword)[0].value = "";
               $(logInPassword).addClass("is-invalid");
               if (data.data == "username") {
                  $(logInEmail).addClass("is-invalid");
                  this.send_error("Username is not correct");
               } else {
                  this.send_error("Password is not correct");
               }
            } else {
               window.location.href = "/feed/";
            }
         });
      },
      signup() {
         let signUpFields = [$(signUpUsername), $(signUpFirstname), $(signUpLastname), $(signUpEmail), $(signUpPassword), $(signUpWeight), $(signUpPasswordConfirm)]
         signUpFields.forEach((field) => {
            field.removeClass("is-invalid");
         });
         let sendData = {
            username: $(signUpUsername)[0].value,
            firstname: $(signUpFirstname)[0].value,
            lastname: $(signUpLastname)[0].value,
            email: $(signUpEmail)[0].value,
            password: $(signUpPassword)[0].value,
            weight: $(signUpWeight)[0].value,
            passwordCheck: $(signUpPasswordConfirm)[0].value,
         };
         fetch("/api/signup/", { method: "POST", credentials: 'same-origin', body: JSON.stringify(sendData) })
         .then((response) => {
           if (!response.ok) throw Error(response.statusText);
           return response.json();
         })
         .then((data) => {
            if (data.status == "failed") {
               if (data.reason == "empty field") {
                  signUpFields.forEach((field) => {
                     if (field[0].value == '') {
                        field.addClass('is-invalid');
                     }
                  });
                  this.send_error("Fields in red are missing");
               }
               if (data.reason == "username duplicate") {
                  $(signUpUsername).addClass('is-invalid');
                  this.send_error("Username already in use");
               }
               if (data.reason == "username invalid character") {
                  $(signUpUsername).addClass('is-invalid');
                  this.send_error("Invalid username character: @ or space")
               }
               if (data.reason == "invalid email") {
                  $(signUpEmail).addClass('is-invalid');
                  this.send_error("Invalid email address");
               }
               if (data.reason == 'passwords are not same') {
                  $(signUpPasswordConfirm).addClass('is-invalid');
                  $(signUpPassword).addClass('is-invalid');
                  this.send_error("Passwords don't match");
               }
               if (data.reason == 'invalid weight') {
                  $(signUpWeight).addClass('is-invalid');
                  this.send_error("Invalid weight");
               }
            } else {
               window.location.href = "/feed/";
            }
         });
      },
   }
};
</script>