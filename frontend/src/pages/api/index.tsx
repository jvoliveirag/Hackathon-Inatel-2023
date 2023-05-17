// pages/api.ts
import { NextApiRequest, NextApiResponse } from 'next';
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:5000/'
const ENDPOIT = 'network-traffic-data'

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  try {
    const response = await axios.get(`${BASE_URL}${ENDPOIT}`);
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch data from the backend.' });
  }
}
