<template>
   <div style="width: 90%; margin-left: auto; margin-right: auto;">
        <h1 style="text-decoration: underline; text-decoration-color: blue; font-size: 4em;">{{displayName}}'s Stats</h1>
        <p style="font-size: 1.5em">Account Created: {{creation_date}}</p>
        <p style="font-size: 1.5em">Calories Burned: <numberdisplay :target="total_cal" style="font-size: 1em"></numberdisplay></p>
        <p style="font-size: 1.5em">Minutes Spent Exercising: <numberdisplay :target="total_min" style="font-size: 1em"></numberdisplay></p>
    </div>
</template>

<script>
module.exports = {
   data: function() {
      return {
          displayName: "",
          total_cal: 0,
          total_min: 0,
          creation_date: "",
      };
   },
   props: ['name'],
   created: function() {
      $(document).ready(() => {
          fetch('/api/u/' + this.name + '/', { credentials: 'same-origin' })
            .then((response) => {
              if (!response.ok) throw Error(response.statusText);
              return response.json();
            })
            .then((data) => {
                console.log(data);
               this.displayName = data.first_name + " " + data.last_name;
               this.total_cal = data.total_calories;
               this.total_min = data.total_minutes;
               this.creation_date = data.created;
            })
            .catch((error) => console.log(error));
      });
   }
};
</script>

<style scoped>
* {
   font-size: 20px;
   padding-top: 10px;
}
.main_text {
   display: inline !important;
}
.dropdown-item {
   font-size: 15px;
}
</style>