<template>
   <div>
      <div class="card">
         <div class="card-body" style="overflow-x: auto; display: inline-block; white-space: nowrap">
            <span style="margin-left: 5px; margin-right: 5px;">Groups selected:</span>
            <template v-for="group in groups">
               <button type="button" class="btn btn-primary" v-if="selected_groups.has(group)" style="margin-right: 5px;" @click="setGroup(group)">{{group}}</button>
               <button type="button" class="btn btn-outline-primary" style="margin-right: 5px;" @click="setGroup(group)" v-else>{{group}}</button>
            </template>
         </div>
      </div>
      <div style="height: 20px;"></div>
      <div class="card" style="width: 90%; margin-left: auto; margin-right: auto">
         <div class="card-header">
            <span>Share what you are doing with all your groups!</span>
         </div>
         <div class="card-body">
            <span>I went </span>
            <input type="text" placeholder="exercise" style="width: 240px" id="exercise_type"></input>
            <span> for </span>
            <input type="number" placeholder="time" style="width: 60px" id="exercise_time"></input>
            <span> minutes. </span>
            <p>
               <span>Do you want to describe your workout?</span>
            </p>
            <textarea style="width: 400px" id="exercise_description"></textarea>
            <p></p>
            <button type="button" class="btn btn-outline-primary" @click="sharePost()">Share!</button>
         </div>
      </div>
      <template v-for="post in posts">
         <div style="height: 20px;"></div>
         <div class="card" style="width: 90%; margin-left: auto; margin-right: auto">
            <div class="card-header">
               <span>{{post.name}} went {{post.exercise}} for {{post.time}} minutes on {{post.date}}</span>
               <span style="float: right;">{{post.calories}} calories</span>
            </div>
            <div class="card-body">
               {{post.body}}
            </div>
         </div>
      </template>
      <div style="height: 20px;"></div>
      <div v-if="share_successful" class="alert alert-success" style="width: 200px; position: fixed; bottom: 0px; margin-left: 50%; transform: translate(-100px, 0px)">
         Successfully shared!
      </div>
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
         posts : [
            {
               name: "Joe",
               exercise: "swimming",
               time: 20,
               date: "11/21/2021",
               calories: 390,
               body: "I went swimming for 20 minutes in the CCRB, freestyle."
            },
            {
               name: "Alex",
               exercise: "running",
               time: 20,
               date: "11/20/2021",
               calories: 180,
               body: "800m warmup, 400m cooldown at 10 minute pace. Ran for 2 miles for workout."
            }
         ],
         share_successful: false,
         groups: ['493 Gainz', '493 Exercise'],
         selected_groups: new Set([ '493 Gainz' ]),
      };
   },
   props: ['name'],
   methods: {
      sharePost() {
         this.posts.unshift({
            name: this.name,
            exercise: $(exercise_type)[0].value,
            time: $(exercise_time)[0].value,
            date: new Date().toLocaleDateString(),
            calories: $(exercise_time)[0].value * 10,
            body: $(exercise_description)[0].value
         });
         this.share_successful = true;
         setTimeout(() => this.share_successful = false, 3000);
      },
      
      setGroup(group) {
         if (this.selected_groups.has(group)) {
            this.selected_groups.delete(group);
         } else {
            this.selected_groups.add(group);
         }
         this.$forceUpdate();
      }
   },
   created: function() {
   }
};
</script>

<style scoped>
</style>