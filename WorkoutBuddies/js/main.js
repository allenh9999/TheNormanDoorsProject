import Vue from 'vue';
import mainmenu from "./mainmenu";
import mainmenudivider from './mainmenudivider';
import feed from './feed';
import mainpage from './mainpage';
import settingspage from './settingspage';
import settingsitem from './settingsitem';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

Vue.component('mainmenu', mainmenu);
Vue.component('mainmenudivider', mainmenudivider);
Vue.component('feed', feed);
Vue.component('mainpage', mainpage);
Vue.component('settingspage', settingspage);
Vue.component('settingsitem', settingsitem);

$(document).ready(() => {
   new Vue({
      el: "#main",
   });
});