import axios from "axios"

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;


class API {
    async getPoints(): any {
        /*
        const data = await axios.get(`${BACKEND_URL}/api/v1/points`);
        return { points: data.data.points, floors: data.data.floors };
        */
        console.log(VITE_BACKEND_URL);
    }
}

export default new API();
