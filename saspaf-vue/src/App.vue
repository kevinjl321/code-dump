<template>
  <div id="app">
    <div id="navbar">
      <div id="nav-container">
        <div class="left">
          <div class="nav-link" id="nav-logo">
            <img :src="require('@/assets/logo.png')" height="80px" />
          </div>
        </div>
        <div class="right">
          <div class="nav-link">
            <a href="" class="left-animate">Home</a>
          </div>
          <div class="nav-link">
            <a href="#impact" class="left-animate">Our Services</a>
          </div>
          <div class="nav-link">
            <router-link to="/join" class="left-animate">Get Involved</router-link>
          </div>
          <div class="nav-link">
            <a href="#" class="left-animate">Contact</a>
          </div>
          <div class="nav-link">
            <a href="#" class="left-animate">Blog</a>
          </div>
          <div class="nav-link">
            <button id="donate-btn-nav" class="button">DONATE</button>
          </div>
        </div>
      </div>
    </div>

    <router-view></router-view>

    <div class="footer-container scew">
      <!--div containing socials and small description-->
      <div class="left-col">
        <p>
          Our mission is to empower the lives of single parent families around
          the nation.
          <br /><br />
          SASPAF is a non-profit organization.
          <a href="#">Donate</a> or <a href="#">volunteer</a> with us!
        </p>

        <div class="social-media">
          <a href="https://www.facebook.com/saspaf/"
            ><i class="fab fa-facebook-f button"></i
          ></a>
          <a href="#"><i class="fab fa-twitter button"></i></a>
          <a href=" https://www.instagram.com/saspaf/"
            ><i class="fab fa-instagram button"></i
          ></a>
          <a href="#"><i class="fab fa-linkedin-in button"></i></a>
          <a
            href="https://greatnonprofits.org/org/support-and-assistance-for-single-parent-families"
            ><i class="fa fa-gratipay button" aria-hidden="true"></i
          ></a>
        </div>
      </div>

      <!--div containing links to above pages-->
      <div class="mid-col">
        <ul id="footer-links">
          <li><a href="/">Home</a></li>
          <li><a href="#info">About Us</a></li>
          <li><a href="#volunteer">Join Us</a></li>
          <li><a href="#donate">Donate</a></li>
          <li><a href="#footer">Contact</a></li>
          <li><a href="#">Blog</a></li>
        </ul>

        <ul id="footer-details">
          <li><a href="#">Privacy Policy</a></li>
          <li><a href="#">Terms of Service</a></li>
          <li><a href="#">Volunteer</a></li>
          <br />
          <li><a href="#">Resources</a></li>
          <li><a href="#">View Reports</a></li>
        </ul>
      </div>

      <!--div containing newsletter sign up-->
      <div class="right-col" id="newsletter">
        <h1>Keep in touch with us!</h1>
        <form id="contact-form">
          <input
            id="email-field"
            type="email"
            name="email"
            placeholder="Email address"
            autocomplete="off"
          />
          <input
            class="button"
            id="submit-contact"
            type="submit"
            value="Join"
          />
        </form>
      </div>
    </div>

    <div id="rights-text">
      &copy; 2020 Support and Assistance for Single Parent Families | Designed
      and developed by Kevin Lan, Tony Xin, & Caleb Kim
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  components: {
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
@import url('https://fontlibrary.org/face/glacial-indifference');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300&display=swap');

* {
  margin: 0;
  box-sizing: border-box;
  outline: 0 !important;
  font-family: var(--main-font-family);
}

:root {
  --main-font-family: 'GlacialIndifferenceRegular', 'Montserrat';
  --secondary-font-family: 'Roboto', sans-serif;
  --main-bg-color: #c7e4df;
  --secondary-bg-color: #68b3a5;
  --third-color: #cff3ec;
  --secondary-section-color: #c1ece4;
  --footer-color: #bbebe3;
}

html {
  scroll-behavior: smooth;
}

button {
  transition: 0.3s all;
}

li {
  list-style: none;
}

a {
  text-decoration: none;
}

.button:hover {
  opacity: 0.5;
  cursor: pointer;
}

button,
input {
  font-family: var(--main-font-family);
}

body {
  background-color: var(--main-bg-color);
  font-family: var(--main-font-family);
  overflow-x: hidden;
}
</style>

<style scoped>
#navbar {
  background-color: rgb(130, 211, 141);
  height: 80px;
  width: 100%;
  top: 0;
  position: absolute;
  padding: 0px 10vw;
  text-align: center;
}

#nav-container {
  width: 1000px;
  display: inline-block;
}

#nav-logo {
  position: relative;
  top: 0px;
}

#donate-btn-nav {
  height: 30px;
  width: 100px;
  font-size: 1rem;
  color: white;
  background-color: transparent;
  border: 2px solid white;
}
.nav-link:not(:last-child) {
  position: relative;
  top: 45px;
  display: inline-block;
  padding: 0px 10px;
  margin-right: 1vw;
}

.nav-link:last-child {
  position: relative;
  top: 42px;
  display: inline-block;
  padding: 0px 10px;
  margin-right: 1vw;
}

.nav-link > a {
  color: rgb(255, 255, 255);
  font-size: 20px;
}

a.left-animate {
  position: relative;
}

a.left-animate:before {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -3px;
  left: 0;
  background-color: rgb(26, 143, 36);
  visibility: hidden;
  transition: all 0.3s ease-in-out;
}

a.left-animate:hover:before {
  visibility: visible;
  width: 100%;
}

.left {
  float: left;
}

.right {
  float: right;
}

footer {
  bottom: 0;
  background: var(--footer-color);
}

.footer-container {
  display: flex;
  flex-wrap: wrap-reverse;
  flex-shrink: 0;
  justify-content: center;
  padding: 20px 50px;
  width: 100%;
}

.left-col {
  width: 300px;
}

.left-col p {
  font-size: 16px;
}

.left-col a {
  color: rgb(103, 129, 103);
}

.mid-col {
  width: 300px;
}

.right-col {
  width: 300px;
}

.social-media {
  margin: 20px 0;
  margin-top: 6vh;
}

.social-media a {
  color: #001a21;
  margin-right: 25px;
  font-size: 20px;
  text-decoration: none;
  transition: 0.3s linear;
}

.mid-col {
  display: flex;
  flex-direction: row;
}

#footer-links li {
  font-size: 16px;
}

#footer-links a {
  color: black;
}

#footer-links li:not(:first-child) {
  margin: 1em 0;
}

#footer-details {
  margin-left: 10px;
  margin-right: 3vw;
}

#footer-details li {
  font-size: 16px;
  font-weight: 1000;
}

#footer-details a {
  color: black;
}

#footer-details li:not(:first-child) {
  margin: 1em 0;
}

#newsletter > h1 {
  font-size: 20px;
  margin: 5px;
}

#rights-text {
  display: flex;
  justify-content: center;
  padding-bottom: 30px;
  font-size: 14px;
  color: gray;
}

#contact-form > #email-field {
  margin-top: 1vh;
  border: none;
  border-bottom: 2px solid white;
  background: transparent;
}

#contact-form > #submit-contact {
  margin-left: 1vw;
  border-radius: 2px;
  background-color: var(--secondary-bg-color);
  width: 3vw;
}

#contact-form > input {
  font-size: 15px;
}

#email-field {
  height: 25px;
  width: 150px;
  border: none;
}

#submit-contact {
  height: 25px;
  width: 50px;
  border: none;
  outline: none;
  transition: 0.3s all;
}
</style>
