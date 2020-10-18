<template>
  <div id="upcoming" class="scew">
    <div class="unscew" style="text-align: center;">
      <div id="upcoming-title">
        <h1>Events & Activities</h1>
      </div>

      <div class="event">
        <div class="event-img">
          <img
            src="https://www.waterville-me.gov/wp-content/uploads/2017/06/volunteer-hands.jpg"
          />
        </div>
        <h1>Event Name</h1>
        <p>Short description of the event</p>
        <button class="button">Participate</button>
      </div>

      <div class="event">
        <div class="event-img">
          <img
            src="https://www.waterville-me.gov/wp-content/uploads/2017/06/volunteer-hands.jpg"
          />
        </div>
        <h1>Event Name</h1>
        <p>Short description of the event</p>
        <button class="button">Participate</button>
      </div>

      <div class="event">
        <div class="event-img">
          <img
            src="https://www.waterville-me.gov/wp-content/uploads/2017/06/volunteer-hands.jpg"
          />
        </div>
        <h1>Event Name</h1>
        <p>Short description of the event</p>
        <button class="button">Participate</button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Upcoming',
  components: {},
}
</script>

<style scoped>
#upcoming {
  background-color: rgb(168, 223, 175);
  padding: 50px 0px;
}

#upcoming-title {
  text-align: center;
  color: white;
  margin: 0 auto;
  margin-top: 2vh;
}

.event {
  width: 300px;
  height: 500px;
  background-color: var(--secondary-bg-color);
  display: inline-block;
  margin: 30px 50px;
  color: white;
}

.event-img img {
  width: 300px;
}

.event-img {
  overflow-y: hidden;
  height: 250px;
}

.event h1 {
  margin: 10px 0px;
}

.event button {
  margin-top: 100px;
  border: 2px solid white;
  border-radius: 2px;
  padding: 10px 10px;
  background-color: transparent;
  color: white;
  font-size: 20px;
  transition: 0.3s all;
}
</style>
