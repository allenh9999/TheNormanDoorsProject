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
            <span style="display: inline-grid">
               <input type="text" placeholder="exercise" style="width: 240px" id="exercise_type"></input>
               <p class="error" v-if="display_exercise_missing">The exercise field is blank</p>
            </span>
            <span> for </span>
            <span style="display: inline-grid">
               <span>
                  <input type="number" placeholder="time" style="width: 60px" id="exercise_time" min="1"></input>
                  <span> minutes. </span>
               </span>
               <p class="error" v-if="display_time_missing">The time field is blank</p>
            </span>
            <p>
               <span>Do you want to describe your workout?</span>
            </p>
            <textarea style="width: 400px" id="exercise_description" placeholder="Describe what you accomplished in this workout."></textarea>
            <p></p>
            <button type="button" class="btn btn-outline-primary" @click="sharePost()">Share!</button>
         </div>
      </div>
      <template v-for="post in posts">
         <template v-if="post.groups.filter(group => selected_groups.has(group)).length != 0">
            <div style="height: 20px;"></div>
            <div class="card" style="width: 90%; margin-left: auto; margin-right: auto">
               <div class="card-header">
                  <span>{{post.name}} went {{post.exercise}} for {{post.time}} {{post.date}}</span>
                  <span style="float: right;">{{post.calories}} calories</span>
               </div>
               <div class="card-body">
                  {{post.description}}
               </div>
            </div>
         </template>
      </template>
      <div style="height: 20px;"></div>
      <div v-if="share_successful" class="alert alert-success" style="width: 200px; position: fixed; bottom: 0px; margin-left: 50%; transform: translate(-100px, 0px); text-align: center">
         Successfully shared!
      </div>
      <div v-if="display_fields_missing" class="alert alert-danger" style="width: 300px; position: fixed; bottom: 0px; margin-left: 50%; transform: translate(-150px, 0px); text-align: center">
         Some of the required fields are blank.
      </div>
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
         posts : [],
         share_successful: false,
         groups: [],
         selected_groups: new Set(),
         display_exercise_missing: false,
         display_time_missing: false,
         display_fields_missing: false,
      };
   },
   props: ['name'],
   methods: {
      
      getPosts() {
         fetch("/api/feed/", { credentials: 'same-origin' })
         .then((response) => {
           if (!response.ok) throw Error(response.statusText);
           return response.json();
         })
         .then((data) => {
            this.selected_groups = new Set(data.groups);
            this.posts = data.posts;
            this.groups = data.groups;
         })
         .catch((error) => console.log(error));
      },
      
      sharePost() {
         if ($(exercise_type)[0].value != "" && $(exercise_time)[0].value != "") {
            let sendData = {
               exercise: $(exercise_type)[0].value,
               time: $(exercise_time)[0].value,
               description: $(exercise_description)[0].value == "" ? "No description." : $(exercise_description)[0].value,
            };
            fetch("/api/post/", { method: "POST", credentials: 'same-origin', body: JSON.stringify(sendData) })
            .then((response) => {
              if (!response.ok) throw Error(response.statusText);
              return response.json();
            })
            .then((data) => {
               this.getPosts();
               $(exercise_type)[0].value = "";
               $(exercise_time)[0].value = "";
               $(exercise_description)[0].value = "";
               this.share_successful = true;
               setTimeout(() => this.share_successful = false, 3000);
            });
            this.display_exercise_missing = false;
            this.display_time_missing = false;
         } else {
            if ($(exercise_type)[0].value == "") {
               this.display_exercise_missing = true;
            } else {
               this.display_exercise_missing = false;
            }
            if ($(exercise_time)[0].value == "") {
               this.display_time_missing = true;
            } else {
               this.display_time_missing = false;
            }
            this.display_fields_missing = true;
            setTimeout(() => this.display_fields_missing = false, 3000);
         }
      },
      
      setGroup(group) {
         if (this.selected_groups.has(group)) {
            this.selected_groups.delete(group);
         } else {
            this.selected_groups.add(group);
         }
         this.$forceUpdate();
      },
   },
   created: function() {
      $(document).ready(() => {
         $(exercise_time).on("keypress", (event) => {
            if (event.which < 48 || event.which > 57) {
               event.preventDefault();
            }
         });
         $(exercise_time).on("cut paste drag", (event) => event.preventDefault());
         this.getPosts();
      });
   }
};
</script>

<style scoped>

.error {
   color: red;
   font-size: 0.7em;
   margin: 0px;
}

.btn-primary:hover {
   color: #c1d9fd;
   background-color: #4991fd;
}

.btn-outline-primary:hover {
   color: #4991fd;
   background-color: #c1d9fd;
}
</style>