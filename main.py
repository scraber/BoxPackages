from boxes import packaging

for i in range(1, 101):
    print(f" Order #{i} \t {packaging.summary_order_boxes(i)}")
