import React, { useState } from 'react';
import axiosInstance from '../lib/axiosInstance';

export default function UploadPage() {
  const [file, setFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [deviceType, setDeviceType] = useState('Web');
  const [userId, setUserId] = useState(1);
  const [uploadStatus, setUploadStatus] = useState('');

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    setPreviewUrl(URL.createObjectURL(selectedFile));
    setUploadStatus('');
  };

  const handleUpload = async () => {
    if (!file) {
      alert('이미지를 선택하세요.');
      return;
    }

    try {
      // 1단계: 이미지 업로드
      const formData = new FormData();
      formData.append('file', file);

      setUploadStatus('📤 이미지 업로드 중...');
      const imageRes = await axiosInstance.post('/upload-image', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'  // 이걸 반드시 명시해야 함
      }
      });

      const { gps_lat, gps_lon, image_url } = imageRes.data;

      // 2단계: crack 등록
      setUploadStatus('📍 균열 데이터 등록 중...');
      await axiosInstance.post('/crack', {
        gps_lat,
        gps_lon,
        image_url,
        user_id: userId,
        device_type: deviceType
      });

      setUploadStatus('✅ 등록 완료!');
    } catch (error) {
      console.error(error);
      setUploadStatus('❌ 등록 실패');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-10 px-4">
      <div className="max-w-xl mx-auto bg-white shadow-md rounded-lg p-6">
        <h1 className="text-2xl font-bold text-blue-800 mb-6 flex items-center">
          <span className="mr-2">📷</span> 균열 이미지 업로드
        </h1>

        {/* 이미지 선택 */}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">이미지 파일</label>
          <input type="file" onChange={handleFileChange} className="w-full border rounded px-3 py-2" />
        </div>

        {/* 미리보기 */}
        {previewUrl && (
          <div className="mb-4">
            <img src={previewUrl} alt="미리보기" className="w-full h-64 object-contain rounded border" />
          </div>
        )}

        {/* 사용자 ID 입력 */}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">사용자 ID</label>
          <input
            type="number"
            value={userId}
            onChange={(e) => setUserId(Number(e.target.value))}
            className="w-full border rounded px-3 py-2"
            placeholder="예: 1"
          />
        </div>

        {/* 장비 유형 선택 */}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">촬영 장비</label>
          <select
            value={deviceType}
            onChange={(e) => setDeviceType(e.target.value)}
            className="w-full border rounded px-3 py-2"
          >
            <option value="Mobile">Mobile</option>
            <option value="Drone">Drone</option>
            <option value="Web">Web</option>
          </select>
        </div>

        {/* 버튼 */}
        <button
          onClick={handleUpload}
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          업로드 및 자동 매칭
        </button>

        {/* 상태 메시지 */}
        {uploadStatus && (
          <p className="mt-4 text-center text-sm text-gray-700 font-semibold">{uploadStatus}</p>
        )}
      </div>
    </div>
  );
}
