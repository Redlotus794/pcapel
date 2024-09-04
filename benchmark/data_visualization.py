import psycopg2
import pandas as pd
import streamlit as st
import altair as alt

# 连接到 PostgreSQL 数据库
conn = psycopg2.connect(
    host="localhost",
    database="benchmark_local",
    user="wangjialong",
    password="123456"
)

# 查询数据
query = """
SELECT id, thread_num, table_size, avg_transaction, avg_read_query, avg_write_query, avg_other_query
FROM sysbench_mysql_results
WHERE thread_num = 1 and id > 1
;
"""

# 使用 Pandas 将查询结果读入数据框
df = pd.read_sql_query(query, conn)

# 关闭数据库连接
conn.close()

# 查看数据框内容
print(df.head())

# 使用 Streamlit 展示数据框
st.title("Sysbench MySQL Results Visualization")

# 将 `table_size` 设置为横轴，将其他 avg 列为纵轴
df_melted = df.melt(id_vars=['table_size'], value_vars=['avg_transaction', 'avg_read_query', 'avg_write_query', 'avg_other_query'],
                    var_name='Metric', value_name='Value')

# 使用 Altair 创建可视化图表
chart = alt.Chart(df_melted).mark_line(point=True).encode(
    x=alt.X('table_size:Q', scale=alt.Scale(domain=[1e5, 1e8]), title='Table Size (Million)',
            axis=alt.Axis(values=[1e5, 1e6, 5e6, 10e6, 20e6, 100e6], format='.1s')),
    y=alt.Y('Value:Q', title="Average Value"),
    color='Metric:N'
).properties(
    title='Average Metrics by Table Size (1 Thread)'
)

# 在 Streamlit 中显示图表
st.altair_chart(chart, use_container_width=True)