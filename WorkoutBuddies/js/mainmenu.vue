<template>
   <div style="background:lime; position: fixed; top: 0; left: 0; right: 0; display: inline-block; padding: 10px;">
      <a class="nav-link main_text" href="/">Workout Buddies</a>
      <p style="color: #0d6efd; float: right; position: relative; padding-right: 5px; padding-top: 0px; margin: 0px;">{{name}}</p>
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
      };
   },
   props: ['name']
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