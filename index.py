import pandas as pd
import os
import numpy as np
import seaborn as sns
import warnings
from scipy import stats
from matplotlib import pylab as plt
from statsmodels.graphics.gofplots import qqplot
from IPython.core.interactiveshell import InteractiveShell

import analysis

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=Warning)
InteractiveShell.ast_node_interactivity = 'all'

def set_seed(seed=42):
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
set_seed()

pd.set_option("display.width", 100)
pd.set_option("display.max_columns", 50)
pd.set_option("display.max_rows", 30)

# Accomodate raw path to variables
raw_customer, raw_orders = "./data/customers.csv", "./data/orders.csv"
raw_products, raw_sales = "./data/products.csv", "./data/sales.csv"

# Read-in data
customer, order = pd.read_csv(raw_customer), pd.read_csv(raw_orders)
product, sales_data = pd.read_csv(raw_products), pd.read_csv(raw_sales)

# ---------- Merging data
cust_order = pd.merge(left=customer, right=order, left_index=True, right_index=True)
cop_data = pd.merge(left=cust_order, right=product, left_index=True, right_index=True)

# ---------- Check Data
# Data đã được làm sạch (không có giá trị nào bị thiếu)
# ----------> Check Data Done

# tính giá trị theo số lượng
cop_data["sales"] = cop_data["price"] * cop_data["quantity"] 
# biểu diễn giá trị ngày, tháng, năm đặt hàng
cop_data["order_date"], cop_data["delivery_date"] = pd.to_datetime(cop_data["order_date"]), pd.to_datetime(cop_data["delivery_date"])
cop_data['year_order'] = cop_data['order_date'].dt.year
cop_data['month_order'] = cop_data['order_date'].dt.month
cop_data["day_order"] = cop_data["order_date"].dt.day

# ------------ Phân tích độ tương quan giữa các trường(giá trị từ -1 đến 1)
# analysis.truc_quan_hoa_tuong_quan(cop_data)
# analysis.truc_quan_hoa_tuong_quan(sales_data)
# -----------> Tổng giá trị đơn hàng phụ thuộc vào giá sản phẩm và số lượng sản phẩm, còn lại những giá trị khác có phụ thuộc nhưng không đáng kể

# ------------ Thống kê
# số lượng, giá trị trung bình,
# độ lệch chuẩn(đo lường mức độ phân tán của dữ liệu so với giá trị trung bình),
# giá trị nhỏ nhất, Giá trị phân vị thứ 25, giá trị trung vị, Giá trị phân vị thứ 75, giá trị lớn nhất
cop_data.describe(include=[np.number])
sales_data.describe(include=[np.number])

# ------------ Phân tích đơn biến
# analysis.phan_tich_don_bien(
#     data=cop_data['sales'],
#     color='red',
#     title1='COP Data - Sales Data Distribution',
#     title2='Quantile Plot')
# analysis.phan_tich_don_bien(
#     data=cop_data['age'],
#     color='red',
#     title1='COP Data - Age Data Distribution',
#     title2='Quantile Plot')
# analysis.phan_tich_don_bien(
#     data=cop_data['price'],
#     color='red',
#     title1='COP Data - Price Data Distribution',
#     title2='Quantile Plot')
# analysis.phan_tich_don_bien(
#     data=cop_data['quantity'],
#     color='red',
#     title1='COP Data - Quantity Data Distribution',
#     title2='Quantile Plot')
# analysis.phan_tich_don_bien(
#     data=sales_data['price_per_unit'],
#     color='red',
#     title1='COP Data - Price per unit Data Distribution',
#     title2='Quantile Plot')
# analysis.phan_tich_don_bien(
#     data=sales_data['total_price'],
#     color='red',
#     title1='COP Data - Total price Data Distribution',
#     title2='Quantile Plot')