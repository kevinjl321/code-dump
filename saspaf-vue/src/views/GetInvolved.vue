<template>
  <div id="get-involved">
    <home></home> 
    <volunteer-info></volunteer-info>
    <donate></donate>
  </div>
</template>

<script>
import VolunteerInfo from '@/components/get-involved/VolunteerInfo.vue'
import Donate from '@/components/Donate.vue'

export default {
  name: 'Home',
  components: {
    home: Home,
    volunteerinfo: VolunteerInfo,
    donate: Donate,
  },
}
</script>

<style scoped>


</style>
