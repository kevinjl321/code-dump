<template>
  <div id="home">
    <div id="home-content">
      <div id="home-text">
        <h1>We are SASPAF.</h1>
        <br />
        <p>
          Serving and empowering single parent families across the nation, one
          service at a time.
        </p>
        <br />
        <button id="home-btn" class="button">Learn More</button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Home',
  components: {},
}
</script>

<style scoped>

#home{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 70vh;
    background-color: rgb(63, 133, 74);
}

#home-text{
    text-align: center;
    width: 45vw;
    color: white;
}

#home-text h1{
    font-size: 3.5rem;
}

#home-text p{
    font-size: 1.5rem;
}

#home-btn{
    margin-top: 2vh;
    width: 7vw;
    height: 5vh;
    font-size: 1rem;
    border: 2px solid white;
    background-color: transparent;
    color: white
}

</style>
