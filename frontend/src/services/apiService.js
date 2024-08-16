import axios from "axios";
import {baseURL} from "../constants/urls";

const apiService = axios.create({baseURL})

apiService.interceptors.request.use(req => {
    const token = localStorage.getItem('access');

    if (token) {
        req.headers.Authorization = `Bearer ${token}`
    }

    return req
})

export {
    apiService
}