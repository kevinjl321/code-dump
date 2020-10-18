<template>
  <div id="mission">
    <div id="mission-content">
      <div id="mission-text">
        <p>
          Support and Assistance for Single Parent families is a student-led
          nonprofit organization dedicated to supporting single-parent families
          with financial assistance, emotional wellness services, employment
          opportunities, educational support, and legislative reforms.
        </p>
      </div>
      <div id="mission-icons">
        <div class="mission-icon">
          <i class="fa fa-heart" aria-hidden="true"></i>
          <br />
          <h2>Goal 1</h2>
        </div>
        <div class="mission-icon">
          <i class="fa fa-heart" aria-hidden="true"></i>
          <h2>Goal 2</h2>
        </div>
        <div class="mission-icon">
          <i class="fa fa-heart" aria-hidden="true"></i>
          <h2>Goal 3</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Mission',
  components: {},
}
</script>

<style scoped>
#mission {
  display: flex;
  justify-content: center;
  background-color: rgb(241, 240, 236);
  height: 45vh;
}

#mission-text {
  margin-top: 5vh;
  text-align: center;
  width: 45vw;
  font-size: 1.5rem;
}

#mission-icons {
  display: flex;
  justify-content: center;
  flex-direction: row;
  margin-top: 3vh;
  width: 45vw;
  text-align: center;
}

#mission-icons i {
  font-size: 3rem;
}

.mission-icon:not(:first-child) {
  margin-left: 5vw;
}
</style>
