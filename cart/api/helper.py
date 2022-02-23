from cart.models import Cart


class Helper:

    def __init__(self, user):
        self.user = user
        self.cart_total_amount = 0
        #self.cart_final_total_amount = 0
        self.cart_products = []
        
        self.checkout_details = {'product': [], 'total': [], 'amount': []}

    def checkout(self):
        self.cart_products = Cart.objects.filter(user=self.user)

        if not self.cart_products:
             return False

        self.calculate_cart_amount()
        self.prepare_checkout_details()

        return self.checkout_details

    
    def calculate_cart_amount(self):
        for cart_product in self.cart_products:
            self.cart_total_amount += cart_product.quantity
   
    def prepare_checkout_details(self):
        for cart_product in self.cart_products:
            self.checkout_details['product'].append({
                                                      
                                                      'product_id': cart_product.id,
                                                      'product_name': cart_product.product,
                                                      'quantity': cart_product.quantity,
                                                      'price': cart_product.product})

        self.checkout_details['total'].append({'total_price': self.cart_total_amount})

        