import Vue from 'vue';
import mainmenu from "./mainmenu";

Vue.component('mainmenu', mainmenu);

$(document).ready(() => {
   new Vue({
      el: "#main",
   });
});