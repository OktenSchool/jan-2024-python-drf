import {useEffect, useState} from "react";
import axios from "axios";

const App = () => {
    const [cars, setCars] = useState([])


    useEffect(() => {
        axios.get('/api/cars').then(({data}) => setCars(data.data))
    }, [])

    return (
        <div>
            <h1>Cars</h1>
            {cars.map(car=><div key={car.id}>{car.id} -- {car.brand}</div>)}
        </div>
    );
};

export {App};