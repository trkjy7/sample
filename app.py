import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# 1️⃣ CSV 파일 불러오기
file_path = "station.csv"
df = pd.read_csv(file_path, encoding="cp949")  # 또는 euc-kr, utf-8 시도 가능

# 2️⃣ 데이터 구조 확인
print(df.head())
print(df.columns)

# 예시 컬럼: ['역명', '시간대', '혼잡도'] 라고 가정
# 실제 파일 컬럼명이 다르면 아래 변수명만 맞게 수정

# 3️⃣ 시간대별 평균 혼잡도 계산
time_congestion = df.groupby("시간대")["혼잡도"].mean().reset_index()

# 4️⃣ 전체 평균 혼잡도 선 그래프
plt.figure(figsize=(10,5))
plt.plot(time_congestion["시간대"], time_congestion["혼잡도"], marker='o')
plt.title("시간대별 평균 혼잡도 추이")
plt.xlabel("시간대")
plt.ylabel("혼잡도(%)")
plt.grid(True)
plt.show()

# 5️⃣ 인터랙티브 Plotly 그래프 (역별 비교)
fig = px.line(df, x="시간대", y="혼잡도", color="역명",
              title="역별 시간대 혼잡도 변화",
              markers=True)
fig.update_layout(legend_title_text="지하철역")
fig.show()

# 6️⃣ 피크 시간대 분석
peak = time_congestion.loc[time_congestion["혼잡도"].idxmax()]
print(f"🚇 가장 혼잡한 시간대: {peak['시간대']} (평균 혼잡도: {peak['혼잡도']:.1f}%)")

low = time_congestion.loc[time_congestion["혼잡도"].idxmin()]
print(f"😌 가장 여유로운 시간대: {low['시간대']} (평균 혼잡도: {low['혼잡도']:.1f}%)")
