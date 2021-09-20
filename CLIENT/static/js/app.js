axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

// console.log('hello')

var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data: {
        years: [],
        prices: [],
        location: '',
        best_fit: [],
    },
    mounted: function() {
        this.years = JSON.parse(document.getElementById('year').textContent)
        this.prices = JSON.parse(document.getElementById('price').textContent)
        this.location = JSON.parse(document.getElementById('location').textContent)
        this.best_fit = JSON.parse(document.getElementById('best_fit').textContent)
        console.log(this.years[0])
        var ctx = document.getElementById('energy_cost_chart').getContext('2d');
        var energy_cost_chart = new Chart(ctx, {
            data: {
                datasets: [
                    {
                        type: 'bar',
                        label: 'Historical Energy Cost at ZIP Code: ' + this.location,
                        data: this.prices,       //Y-axis
                        options: {
                            trendlineLinear: {
                            style: "rgba(255,105,180, .8)",
                            lineStyle: "dotted|solid",
                            width: 2
                            }
                        }
                    },
                    {
                        type: 'line',
                        label: 'Projected Energy Cost at ZIP Code: ' +this.location,
                        data: this.best_fit,
                    }
                ],
                labels: this.years,     //X-axis
            },
            // options: {
            //     scales: {
            //         x: {
            //             min: this.years[0] + 25
            //         }
            //     }
            // },
        })
    },
});

var solar = new Vue({
    el: '#solar',
    delimiters: ["[[", "]]"],
    data: {
        panel_width: 35,
        panel_height: 69,
        panels: 1,
        ghi: 0,
        degredation: 0.05,
        efficiency: 0.20,
    },
    mounted: function() {
        this.ghi = JSON.parse(document.getElementById('ghi').textContent)
        // console.log(this.ghi)
    },
    methods: {
        calculate: function() {
            let pw_meter = this.panel_width * 0.0254
            let ph_meter = this.panel_height * 0.0254
            let panel_area = pw_meter * ph_meter
            console.log(pw_meter)
            console.log(ph_meter)
            console.log(panel_area)

            let i_kwh_year = this.ghi*panel_area*this.panels*this.efficiency
            console.log(i_kwh_year)
        }
    }
});