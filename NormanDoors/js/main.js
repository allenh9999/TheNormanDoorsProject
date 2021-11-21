import Vue from 'vue';
import MainMenu from "./mainmenu";

Vue.component('MainMenu', MainMenu);

$(document).ready(() => {
   new Vue({
      el: "#main",
      template: "<MainMenu/>",
   });
});