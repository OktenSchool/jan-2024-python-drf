import {CarForm} from "../components/CarForm";
import {Cars} from "../components/Cars";
import {Chat} from "../components/Chat";

const CarPage = () => {
    return (
        <div>
            <CarForm/>
            <hr/>
            <Cars/>
            <hr/>
            <Chat/>
        </div>
    );
};

export {CarPage};