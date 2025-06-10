import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 查询并打印表格内容
tables = [
    'Categories', 'Diseases', 'Symptoms', 'Interventions', 'Biomarkers',
    'Comorbidities', 'Diagnoses', 'DifferentialDiagnoses', 'Measurements', 'RiskFactors',
    'Disease_Symptoms', 'Disease_Interventions', 'Disease_Biomarkers', 'Disease_Comorbidities',
    'Disease_Diagnoses', 'Disease_DifferentialDiagnoses', 'Disease_Measurements', 'Disease_RiskFactors'
]
for table in tables:
    cursor.execute(f'SELECT * FROM {table};')
    print(f'{table}:')
    print(cursor.fetchall())

# 关闭连接
conn.close()