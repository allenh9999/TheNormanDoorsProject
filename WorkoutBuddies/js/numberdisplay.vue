<template>
   <span>{{number}}</span>
</template>

<script>
module.exports = {
   data: function() {
      return {
          number: 0,
          floatNumber: 0,
          timeout: null,
      };
   },
   props: ['target'],
   methods: {
      getCloser() {
         if (this.target <= this.floatNumber) {
            this.number = this.target;
            this.floatNumber = this.target;
            return;
         }
         this.floatNumber += Math.max(0.05, (this.target - this.floatNumber) / Math.log(Math.abs(this.target) + 1.01));
         this.number = Math.floor(this.floatNumber);
         this.timeout = setTimeout(this.getCloser, 16);
      },
      start() {
         clearTimeout(this.timeout);
         this.timeout = setTimeout(this.getCloser, 16);
      },
   },
   watch: {
      target: function() {
         this.start();
      }
   },
   created: function() {
      $(document).ready(() => {
         this.start();
      });
   },
};
</script>
