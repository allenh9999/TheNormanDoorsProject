import Vue from 'vue';
import mainmenu from "./mainmenu";
import mainmenudivider from './mainmenudivider';
import feed from './feed'
import 'bootstrap/dist/css/bootstrap.min.css';

Vue.component('mainmenu', mainmenu);
Vue.component('mainmenudivider', mainmenudivider);
Vue.component('feed', feed);

$(document).ready(() => {
   new Vue({
      el: "#main",
   });
});