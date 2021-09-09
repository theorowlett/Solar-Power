axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

console.log('hello')

var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
        states: ['Alabama','Alaska','American Samoa','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Federated States of Micronesia','Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Palau','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
    },
    mounted: function() {
        // var ctx = document.getElementById('energy-cost-chart');
        // var energy_cost_chart = new CharacterData(ctx, {
        //     type: 'bar',
        //     data: {
        //         labels: '',
        //         datasets: [{
        //             label: 'cost per kWh',
        //             data: '',
        //         }]
        //     }
        // })
        // console.log(years);
    },
    methods: {
        profile: function(id) {
            edit_profile(id);
        },
    },
});

let edit_profile = function(id) {
    $("#profile-dialog").modal('show');
    let state = document.querySelector('#state').value;
    let add1 = document.querySelector('#add1').value;
    let add2 = document.querySelector('#add2').value;
    let zip = document.querySelector('#zip').value;
    let email = document.querySelector('#email').value;
    console.log(state);
    
    let cancel_btn = document.querySelector('#close-profile');
    cancel_btn.addEventListener('click', function(){
        $("#profile-dialog").modal('hide');
    });
    
    let update_btn = document.querySelector('#update-profile');
    update_btn.addEventListener('click', function(){
        axios.put('http://localhost:8000/API/' + id + '/',{
             'username': 'theo',
             'state': state,
             'address1': add1,
             'address2': add2,
             'zip': zip,
             'email': email,
            })
        .then(function (response){
            $("#profile-dialog").modal('hide');
        })
    });
}


var app = new Vue({
    el: '#profile-dialog',
    delimiters: ["[[", "]]"],
    data: {
        states: ['Alabama','Alaska','American Samoa','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','District of Columbia','Federated States of Micronesia','Florida','Georgia','Guam','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Marshall Islands','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Northern Mariana Islands','Ohio','Oklahoma','Oregon','Palau','Pennsylvania','Puerto Rico','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virgin Island','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
    },
});
