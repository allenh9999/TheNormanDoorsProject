<template>
   <div style="background:black; position: fixed; top: 0; left: 0; right: 0; display: inline-block; padding: 10px;">
      <a class="nav-link main_text" href="/">Workout Buddies</a>
      <a class="nav-link main_text" style="float: right; position: relative; padding-right: 5px; padding-top: 0px; margin: 0px;" :href="'/u/' + name + '/'">{{displayName}}</a>
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
         displayName: "",
      };
   },
   props: ['name'],
   created: function() {
      $(document).ready(() => {
         if (name != "") {
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
</style>