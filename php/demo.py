from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id='mch61a7267b62a08', sslc_store_pass='mch61a7267b62a08@ssl')

mypayment.set_urls(success_url='example.com/success', fail_url='example.com/failed', cancel_url='example.com/cancel', ipn_url='example.com/payment_notification')

mypayment.set_product_integration(total_amount=Decimal('20.20'), currency='BDT', product_category='clothing', product_name='demo-product', num_of_item=2, shipping_method='YES', product_profile='None')

mypayment.set_customer_info(name='Pravin Kumar', email='pravinkumar@gmail.com', address1='Mirpur', address2='Dhaka', city='Dhaka', postcode='1207', country='Bangladesh', phone='01711111456')

mypayment.set_shipping_info(shipping_to='Pravin Kumar', address='Mirpur', city='Dhaka', postcode='1209', country='Bangladesh')

# If you want to post some additional values
mypayment.set_additional_values(value_a='aaw@gmail.com', value_b='portalcustomerid', value_c='1234', value_d='uuid')

response_data = mypayment.init_payment()

print(response_data["GatewayPageURL"])