import React, { useEffect, useState } from 'react';
import axiosInstance from '../lib/axiosInstance';

const Dashboard = () => {
  const [cracks, setCracks] = useState([]);

  useEffect(() => {
    axiosInstance.get('/crack')
      .then((res) => setCracks(res.data))
      .catch((err) => console.error('불러오기 실패:', err));
  }, []);

  return (
    <div className="min-h-screen bg-gray-50 py-10 px-6">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-2xl font-bold text-gray-800 flex items-center mb-6">
          <span className="mr-2">📋</span> 균열 등록 내역
        </h1>
        <p className="text-sm text-gray-500 mb-4">ID 이미지 위도 경도 농수로 번호 자동 매칭</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {cracks.map((crack) => (
            <div key={crack.crack_id} className="bg-white rounded-lg shadow p-4 border hover:shadow-md">
              <img src={crack.image_url} alt="crack" className="w-full h-48 object-cover rounded mb-3" />
              <p className="text-sm">🆔 ID: {crack.crack_id}</p>
              <p className="text-sm">📍 위도: {crack.gps_lat}</p>
              <p className="text-sm">📍 경도: {crack.gps_lon}</p>
              <p className="text-sm">🔗 농수로 번호: <span className="font-semibold">{crack.canal_number || '-'}</span></p>
              <p className="text-sm">🤖 자동 매칭: {crack.auto_matched ? '✅' : '❌'}</p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;