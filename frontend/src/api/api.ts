import axios from "axios";

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL;

class API {
  //   async getPoints(): any {
  //     /*
  //         const data = await axios.get(`${BACKEND_URL}/api/v1/points`);
  //         return { points: data.data.points, floors: data.data.floors };
  //         */
  //     console.log(VITE_BACKEND_URL);
  //   }

  async getBowlingAlleys(): any {
    const response = await fetch(
      `${BACKEND_URL}/api/v1/bowling_alleys/?skip=0&limit=10`
    );

    const data = response.json();
    return { id: data.data.id, name: data.data.name };
  }
}

export default new API();
