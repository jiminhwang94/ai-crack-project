import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000', // 배포 시 Azure API 주소로 변경
  headers: {
    'Content-Type': 'application/json',
  },
});

export default instance;