const baseURL = '/api'

const auth = '/auth'
const cars = '/cars'

const urls = {
    auth: {
        login: auth,
        socket: `${auth}/token`
    },
    cars
}

export {
    baseURL,
    urls
}
