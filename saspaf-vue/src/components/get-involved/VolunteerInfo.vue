<template>
    <div id = "get-involved">  
        <div id = "join-text">
            <h1>Get Involved</h1>
            <br>
            <p>
            There are so many ways to help, whether it be attending an event or starting
            a chapter in your area!
            </p>
            <hr>
        </div>
        <div id = "volunteer">
            <div id = "volunteer-text">
                <h2>Volunteer with Us!</h2><br>
                <p>
                    Join us at one of our events! You can help by packaging meals, donating 
                    common household items, or by giving the gift of education to the less fortunate.
                    Kind acts do not go unnoticed.
                </p>
                <button id = "volunteer-btn" class = "button">Learn More</button>
            </div>
            <div id = "volunteer-img">
                    INSERT IMAGE
            </div>
        </div>
        <div id = "chapter">
            <div id = "chapter-text">
                <h2>Find a Chapter</h2>
                <br>
                <p>
                    Interested in bringing the impact of SASPAF to a community near you? 
                    Check out the interactive map on the right! If your community is not listed,
                    start a chapter!
                </p>
                <button id = "chapter-btn" class = "button">Learn More</button>
            </div>
            <div id = "map"></div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'VolunteerInfo',
        components: {},
    }
</script>

<style scoped>
    #img-div{
        text-align: center;
        margin-top: 8vh;
        height: 15vh;
        width: 100%;
    }

    #get-involved{
        display: flex;
        align-items: center;
        height: 135vh;
        background-color:rgb(221, 243, 214);
        flex-direction: column;
    }

    #join-text{
        margin-top: 3vh;
        width: 55vw;
    }

    #join-text h1{
        font-size: 3.5rem;
    }

    #join-text p{
        font-size: 1.5rem;
    }

    #join-text hr{
        margin-top: 1vh;
        height: 0.2vh;
        background-color: black;
    }

    #volunteer{
        display: flex;
        justify-content: center;
        flex-direction: row;
        margin-top: 5vh;
    }

    #volunteer-text{
        width: 20vw;
        font-size: 1.5rem;
    }

    #volunteer-img{
        margin-left: 5vw;
        width: 30vw;
    }

    #volunteer-btn{
        margin-top: 2vh;
        width: 8vw;
        height: 3vw;
        text-transform: uppercase;
        font-size: 1rem;
        border: 2px solid white;
        color: white;
        background-color: var(--secondary-bg-color);
    }

    #chapter{
        display: flex;
        justify-content: center;
        flex-direction: row;
        margin-top: 7vh;
    }

    #chapter-text{
        width: 20vw;
        font-size: 1.5rem;
    }

    #chapter-btn{
        margin-top: 2vh;
        width: 8vw;
        height: 3vw;
        text-transform: uppercase;
        font-size: 1rem;
        border: 2px solid white;
        color: white;
        background-color: var(--secondary-bg-color);
    }

    #map{
        width: 30vw;
        margin-left: 5vw;
        height: 50vh;
        border: 2px solid var(--secondary-bg-color);
        border-radius: 5px;
    }

</style>