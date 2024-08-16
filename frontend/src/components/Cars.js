import {useEffect, useState} from "react";
import {carService} from "../services/carService";
import {Car} from "./Car";
import {socketService} from "../services/socketService";

const Cars = () => {
    const [cars, setCars] = useState([])
    const [trigger, setTrigger] = useState(null)

    useEffect(() => {
        carService.getAll().then(({data}) => setCars(data))
    }, [trigger]);

    useEffect(() => {
        socketInit().then()
    }, [])

    const socketInit = async () => {
        const {car} = await socketService();
        const client = await car();

        client.onopen = () => {
            console.log('CarSocket connected');
            client.send(JSON.stringify({
                action: 'subscribe_to_car_activity',
                request_id: new Date().getTime()
            }))
        }
        client.onmessage = () => {
            setTrigger(prev => !prev)
        }

    }
    return (
        <div>
            {cars.map(car => <Car key={car.id} car={car}/>)}
        </div>
    );
};

export {Cars};