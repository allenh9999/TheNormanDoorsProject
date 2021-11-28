<template>
   <div>
      <p>{{setting}}: {{value}}
         <button type="button" class="btn btn-primary" @click="showEdit = false" v-if="showEdit">Edit</button>
         <button type="button" class="btn btn-outline-primary" @click="showEdit = true" v-else>Edit</button>
      </p>
      <template v-if="showEdit">
         <div class="form-floating" style="display: inline-flex;">
            <input :type="type" class="form-control" :id="setting" :placeholder="'new' + setting" style="width: 300px; display: inline">
            <label :for="setting">New {{setting}}</label>
            <button type="submit" class="btn btn-outline-primary" style="height: 58px" @click="setSetting()">Update</button>
         </div>
         <div style="height: 20px">
         </div>
      </template>
   </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
         showEdit: false,
      };
   },
   methods: {
      setSetting() {
         document.getElementById(this.setting).classList.remove("is-invalid");
         let sendData = {
            field: this.setting,
            value: document.getElementById(this.setting).value,
         };
         fetch("/api/settings/", { method: "POST", credentials: 'same-origin', body: JSON.stringify(sendData) })
         .then((response) => {
           if (!response.ok) throw Error(response.statusText);
           return response.json();
         })
         .then((data) => {
            if (data.status == "failed") {
               document.getElementById(this.setting).classList.add("is-invalid");
            } else {
               this.$emit("value", data.value);
            }
         });
      }
   },
   props: ['setting', 'type', 'value']
};
</script>

<style scoped>
</style>