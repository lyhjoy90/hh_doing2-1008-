async function requestDRTReservation() {
    const userId = document.getElementById('userId').value;
    const seatId = document.getElementById('seatId').value;
    const resultBox = document.getElementById('resultBox');
    const resultContent = document.getElementById('resultContent');

    resultContent.innerText = "GPS 위치 수집 중...";
    resultBox.classList.remove('hidden');

    // 테스트용 GPS 위치 설정 (군산/신도시 좌표 예시)
    const payload = {
        user_id: userId,
        seat_id: seatId,
        latitude: 35.9677,
        longitude: 126.7366
    };

    try {
        const response = await fetch('http://localhost:8000/api/v1/drt/reserve', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        resultContent.innerText = JSON.stringify(data, null, 2);
    } catch (error) {
        resultContent.innerText = "❌ 서버 통신 오류: " + error.message;
    }
}