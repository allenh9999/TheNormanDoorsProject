<template>
   <div style="background:black; position: fixed; top: 0; left: 0; right: 0; display: inline-block; padding: 10px; z-index: 10;" @mouseleave="showPanel=false; logoutPrompt=false">
      <a class="nav-link main_text" href="/">Workout Buddies</a>
      <a class="nav-link main_text" style="float: right; position: relative; padding-right: 5px; padding-top: 0px; margin: 0px;" :href="'/u/' + name + '/'" v-if="name != null" @mouseover="showPanel=true">{{displayName}}</a>
      <ul class="dropdown-menu" style="display: block; margin-top: 17px; position: absolute; right: 0px; margin-right: 10px" v-if="name != null && showPanel">
         <a href="/settings/" style="text-decoration: none">
            <p class="dropdown-item">Settings</p>
         </a>
         <div class="dropdown-item" v-if="logoutPrompt">
            <p style="font-size: 15px">You sure you want to logout?</p>
            <button type="button" class="btn btn-outline-primary" @click="logout()">Yes</button>
            <button type="button" class="btn btn-outline-primary" @click="logoutPrompt=false">No</button>
         </div>
         <p class="dropdown-item" v-else @click="logoutPrompt=true">Logout</p>
      </ul>
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
         displayName: "",
         showPanel: false,
         logoutPrompt: false,
      };
   },
   props: ['name'],
   created: function() {
      $(document).ready(() => {
         if (this.name != null) {
            fetch('/api/name/', { credentials: 'same-origin' })
            .then((response) => {
              if (!response.ok) throw Error(response.statusText);
              return response.json();
            })
            .then((data) => {
               this.displayName = data.firstname;
            })
            .catch((error) => console.log(error));
         }
      });
   },
   methods: {
      logout() {
         fetch('/api/logout/', { credentials: 'same-origin' })
         .then((response) => {
           if (!response.ok) throw Error(response.statusText);
           return response.json();
         })
         .then((data) => {
            window.location.replace("/");
         })
         .catch((error) => console.log(error));
      },
   }
};
</script>

<style scoped>
* {
   font-size: 20px;
   padding-top: 10px;
}
.main_text {
   display: inline !important;
}
.dropdown-item {
   font-size: 15px;
}
</style>