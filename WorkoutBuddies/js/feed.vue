<template>
   <div>
      <div class="card">
         <div class="card-body" style="overflow-x: auto; display: inline-block; white-space: nowrap">
            <span style="margin-left: 5px; margin-right: 5px;">Groups selected:</span>
            <template v-for="group in groups">
               <button type="button" class="btn btn-primary" v-if="selected_groups.has(group)" style="margin-right: 5px;" @click="setGroup(group)">{{group}}</button>
               <button type="button" class="btn btn-outline-primary" style="margin-right: 5px;" @click="setGroup(group)" v-else>{{group}}</button>
            </template>
            <button type="button" class="btn btn-success" v-if="add_group" @click="add_group = !add_group;">Add new group</button>
            <button type="button" class="btn btn-outline-success" @click="add_group = !add_group; create_new_group = false; add_existing_group = false;" v-else>Add new group</button>
         </div>
      </div>
      <div class="card" v-if="add_group">
         <div class="card-body">
            <button type="button" class="btn btn-success" v-if="create_new_group" @click="create_new_group = !create_new_group">Create new group</button>
            <button type="button" class="btn btn-outline-success" v-else @click="create_new_group = !create_new_group; add_existing_group = false;">Create new group</button>
            <button type="button" class="btn btn-success" v-if="add_existing_group" @click="add_existing_group = !add_existing_group">Add existing group</button>
            <button type="button" class="btn btn-outline-success" v-else @click="add_existing_group = !add_existing_group; create_new_group = false">Add existing group</button>
            <div v-if="add_existing_group ^ create_new_group">
               <span>This action will lead you to a different page. Continue?</span>
               <button type="button" class="btn btn-outline-success" @click="addNewGroup()">Yes</button>
            </div>
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
               <input type="text" placeholder="exercise" :style="exercise_type_style" @input="checkExercise()" @blur="exitExercise()" id="exercise_type"></input>
               <ul class="dropdown-menu" style="display: block; margin-top: 30px; width: 240px" v-if="exercise_visible">
                  <template v-for="exercise in exercise_type">
                     <p class="dropdown-item" @click="changeExercise(exercise)" v-html="getBolded(exercise)">{{exercise}}</p>
                  </template>
               </ul>
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
            <template v-if="new_exercise">
               <br/>
               <span>This is a new exercise in our system. Do you want to add it?</span>
               <button type="button" class="btn btn-primary" v-if="add_exercise" @click="add_exercise=false">Yes</button>
               <button type="button" class="btn btn-outline-primary" @click="add_exercise=true" v-else>Yes</button>
            </template>
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
                  <a class="nav-link" style="display: inline; padding: 0px;" :href="'/u/' + post.username + '/'">{{post.name}}</a>
                  <span> went {{post.exercise}} for {{post.time}} {{post.date}}</span>
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
         {{error_message}}
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
         exercise_visible: false,
         exercise_type: [],
         exercise_type_style: {
            width: '240px',
         },
         add_exercise: false,
         new_exercise: false,
         error_message: "Some of the required fields are blank.",
         add_group: false,
         create_new_group: false,
         add_existing_group: false,
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
      
      sendPost() {
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
            this.display_fields_missing = false;
            this.exercise_type_style.color = '#000000';
            setTimeout(() => this.share_successful = false, 6000);
            this.add_exercise = false;
            this.new_exercise = false;
         });
      },
      
      sharePost() {
         if ($(exercise_type)[0].value != "" && $(exercise_time)[0].value != "") {
            if (this.new_exercise & !this.add_exercise) {
               this.display_exercise_missing = false;
               this.display_time_missing = false;
               this.error_message = "Either select yes or change the exercise.";
               this.display_fields_missing = true;
               setTimeout(() => this.display_fields_missing = false, 6000);
            } else {
               this.sendPost();
            }
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
            this.error_message = "Some of the required fields are blank.";
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
      
      checkExercise() {
         fetch("/api/getExercises?query=" + $(exercise_type)[0].value, { method: "GET", credentials: "same-origin" })
         .then(response => {
            if (!response.ok) throw Error(response.statusText);
            return response.json();
         })
         .then(data => {
            this.exercise_type = data.exercises;
            if (data.exercises.length != 0) {
               this.exercise_visible = true;
            } else {
               this.exercise_visible = false;
            }
         });
         this.new_exercise = false;
         this.exercise_type_style.color = '#000000';
      },
      
      exitExercise() {
         setTimeout(() => {
            this.exercise_visible = false;
            if (!this.exercise_type.includes($(exercise_type)[0].value) && $(exercise_type)[0].value != "") {
               this.new_exercise = true;
               this.add_exercise = false;
            }
         }, 200);
      },
      
      changeExercise(exercise) {
         $(exercise_type)[0].value = exercise;
         this.exercise_type_style.color = '#555555';
      },
      
      getBolded(exercise) {
         let exerciseRegEx = new RegExp($(exercise_type)[0].value, 'g');
         return exercise.replace(exerciseRegEx, '<b>' + $(exercise_type)[0].value + '</b>');
      },
      
      addNewGroup() {
         if (this.add_existing_group) {
            window.location.href = "/addgroup";
         } else {
            window.location.href = "/creategroup";
         }
      }
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

.btn-outline-success:hover {
   color: #439e73;
   background-color: #d5ffec;
}

.btn-success:hover {
   color: #d5ffec;
   background-color: #439e73;
}
</style>