import Vue from 'vue';
import mainmenu from "./mainmenu";
import mainmenudivider from './mainmenudivider';
import feed from './feed';
import creategroup from './creategroup';
import addgroup from './addgroup';
import mainpage from './mainpage';
import settingspage from './settingspage';
import settingsitem from './settingsitem';
import userinfo from './userinfo';
import numberdisplay from './numberdisplay';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

Vue.component('mainmenu', mainmenu);
Vue.component('mainmenudivider', mainmenudivider);
Vue.component('feed', feed);
Vue.component('mainpage', mainpage);
Vue.component('creategroup',creategroup);
Vue.component('addgroup',addgroup);
Vue.component('settingspage', settingspage);
Vue.component('settingsitem', settingsitem);
Vue.component('userinfo', userinfo);
Vue.component('numberdisplay', numberdisplay);

$(document).ready(() => {
   new Vue({
      el: "#main",
   });
});