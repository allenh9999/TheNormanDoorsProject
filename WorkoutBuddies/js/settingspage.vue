<template>
   <div style="width: 90%; margin-left: auto; margin-right: auto">
      <div style="height: 20px"></div>
      <h1>Settings for {{user_details.username}}</h1>
      <div style="height: 20px"></div>
      <div>
         <p>password:
            <button type="button" class="btn btn-primary" @click="showEdit = false" v-if="showEdit">Edit</button>
            <button type="button" class="btn btn-outline-primary" @click="showEdit = true" v-else>Edit</button>
         </p>
         <template v-if="showEdit">
            <div class="form-floating">
               <input type="password" class="form-control" id="passwordOld" placeholder="Old password" style="width: 300px; display: inline">
               <label for="password">Old password</label>
            </div>
            <div style="height: 20px"></div>
            <div class="form-floating">
               <input type="password" class="form-control" id="password" placeholder="New password" style="width: 300px; display: inline">
               <label for="password">New password</label>
            </div>
            <div style="height: 20px"></div>
            <div class="form-floating">
               <input type="password" class="form-control" id="passwordConfirm" placeholder="New password" style="width: 300px; display: inline">
               <label for="password">Confirm password</label>
            </div>
            <div style="height: 20px"></div>
            <button type="submit" class="btn btn-outline-primary" style="height: 58px" @click="setPassword()">Update</button>
            <div style="height: 20px">
            </div>
         </template>
      </div>
      <settingsitem setting="weight" type="number" :value="user_details.weight" @value="updateWeight"></settingsitem>
      <settingsitem setting="first name" type="text" :value="user_details.firstname" @value="updateFirstname"></settingsitem>
      <settingsitem setting="last name" type="text" :value="user_details.lastname" @value="updateLastname"></settingsitem>
      <settingsitem setting="email" type="text" :value="user_details.email" @value="updateEmail"></settingsitem>
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
         showEdit: false,
         user_details: {
            username: '',
            weight: 0,
         }
      };
   },
   methods: {
      setPassword() {
         $(password).removeClass('is-invalid');
         $(passwordOld).removeClass('is-invalid');
         $(passwordConfirm).removeClass('is-invalid');
         let sendData = {
            field: "password",
            value: $(password)[0].value,
            passwordOld: $(passwordOld)[0].value,
            passwordCheck: $(passwordConfirm)[0].value,
         };
         fetch("/api/settings/", { method: "POST", credentials: 'same-origin', body: JSON.stringify(sendData) })
         .then((response) => {
           if (!response.ok) throw Error(response.statusText);
           return response.json();
         })
         .then((data) => {
            if (data.status == "failed") {
               if (data.reason == "Blank field") {
                  $(password).addClass('is-invalid');
               } else if (data.reason == "passwords do not match") {
                  $(password).addClass('is-invalid');
                  $(passwordConfirm).addClass('is-invalid');
               } else {
                  $(passwordOld).addClass('is-invalid');
               }
            }
         });
      },
      updateWeight(value) {
         this.user_details.weight = value;
      },
      updateFirstname(value) {
         this.user_details.firstname = value;
      },
      updateLastname(value) {
         this.user_details.lastname = value;
      },
      updateEmail(value) {
         this.user_details.email = value;
      }
   },
   created() {
      fetch("/api/settings/", { credentials: 'same-origin' })
      .then((response) => {
        if (!response.ok) throw Error(response.statusText);
        return response.json();
      })
      .then((data) => {
         this.user_details = data;
      });
   },
};
</script>

<style scoped>

</style>