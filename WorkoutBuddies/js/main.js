import Vue from 'vue';
import mainmenu from "./mainmenu";
import mainmenudivider from './mainmenudivider';
import 'bootstrap/dist/css/bootstrap.min.css';

Vue.component('mainmenu', mainmenu);
Vue.component('mainmenudivider', mainmenudivider);

$(document).ready(() => {
   new Vue({
      el: "#main",
   });
});