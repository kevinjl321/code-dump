<template>
  <div id="impact">
    <div id="impact-content">
      <div id="impact-text">
        <h1>Community Impact</h1>
        <br />
        <p>
          !CHANGE THIS Support and Assistance for Single Parent families is a
          student-led nonprofit organization dedicated to supporting
          single-parent families with financial assistance, emotional wellness
          services, employment opportunities, educational support, and
          legislative reforms.
        </p>
        <br />
      </div>

      <div id="stats">
        <div id="stats-container">
          <div class="stat">
            <i class="fa fa-heart" aria-hidden="true"></i>
            <br />
            <h1>400</h1>
            <p>meals provided</p>
          </div>

          <div class="stat">
            <i class="fa fa-heart" aria-hidden="true"></i>
            <br />
            <h1>$8000</h1>
            <p>fundraised</p>
          </div>

          <div class="stat">
            <i class="fa fa-heart" aria-hidden="true"></i>
            <br />
            <h1>7</h1>
            <p>communities helped</p>
          </div>

          <div class="stat">
            <i class="fa fa-heart" aria-hidden="true"></i>
            <br />
            <h1>2500</h1>
            <p>families helped</p>
          </div>

          <div class="stat">
            <i class="fa fa-heart" aria-hidden="true"></i>
            <br />
            <h1>450+</h1>
            <p>service hours committed</p>
          </div>
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
#impact {
  display: flex;
  justify-content: center;
  height: 65vh;
  background-color: var(--secondary-section-color);
}

#impact-content {
  margin-top: 5vh;
  flex-direction: column;
}

#impact-text {
  text-align: center;
  width: 45vw;
}

#impact-text p {
  font-size: 1.5rem;
}

#stats {
  display: flex;
  justify-content: center;
  width: 45vw;
}

#stats-container {
  display: flex;
  flex-direction: row;
  margin-top: 3vh;
}

.stat {
  text-align: center;
}

.stat:not(:last-child) {
  margin-right: 5vw;
  font-size: 1rem;
}

.stat i {
  display: flex;
  justify-content: center;
  font-size: 3.5rem;
}
</style>
