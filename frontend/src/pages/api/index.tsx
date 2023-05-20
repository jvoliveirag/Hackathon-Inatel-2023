// pages/api.ts
import { NextApiRequest, NextApiResponse } from 'next';
import axios from 'axios';

const BASE_URL = 'http://localhost:8080/api/'
const ENDPOIT = 'network-traffic-data'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  console.log("API called");
  try {
    const response = await axios.get(`${BASE_URL}`);
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch data from the backend.' });
  }
}
