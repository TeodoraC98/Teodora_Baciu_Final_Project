
const { getJson } = require("serpapi");
const util =requiew('util');
require('dotenv').config();
getJson({
"api_key":"ae8b0609cf2e9a717bead942e12fbe2930602873ad2dfcbddd68e68ea539abd2",
          "engine":"google_flights",
          "departure_id":"JFK",
          "arrival_id":"AUS",
          "outbound_date":"2025-10-10",
           "return_date":"2015-10-12",
}),results=>{
console.log(util.inspect(results))
}

//  async function handleSubmit() {
//          results = await getJson({
//           "api_key":"ae8b0609cf2e9a717bead942e12fbe2930602873ad2dfcbddd68e68ea539abd2",
//           "engine":"google_flights",
//           "departure_id":"JFK",
//           "arrival_id":"AUS",
//           "outbound_date":"2025-10-10",
//            "return_date":"2015-10-12",
//         });
//         console.log('Best Flights\n');
//         results.best_flights.forEach(item => {
//             item.flights.forEach(flight => {
//                 console.log(
//                     `Flight Number: ${flight.flight_number} | Departure: ${flight.departure_airport.id} (${flight.departure_airport.time}) -> Arrival: ${flight.arrival_airport.id} (${flight.arrival_airport.time}) | Airline: ${flight.airline} | Duration: ${flight.duration} minutes | Airplane: ${flight.airplane} | Total Duration: ${item.total_duration} minutes | Price: ${item.price} ${results.search_parameters.currency} | Type: ${item.type}`
//                 );
//             });
//         });
//     }

class WelcomeBack extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            departure: 'dep',
        }
        this.updateInput = this.updateInput.bind(this);  
    }
       updateInput(event){
         this.setState({departure : event.target.value})
            }
       
    render(){
        return(
            <>
            <input type="date" onChange={this.updateInput}></input>
            <input type="submit" onClick={handleSubmit()} ></input>
            <p>{this.state.departure} </p>
                {/* <h2>Hello {this.state.name || 'Friend'}! Welcome Back.</h2>
                {
                    this.state.apppVersion && this.state.apppVersion < 2
                    ? <p>Your app is out of date. Please download the new version and take a look at all the new features.</p> 
                    : ''
                } */}
            </>
        )
    }


}