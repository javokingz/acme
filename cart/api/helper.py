from cart.models import Cart


class CartHelper:

    def __init__(self, user):
        self.user = user
        self.cart_total_amount = 0
        #self.cart_final_total_amount = 0
        self.cart_products = []
        
        self.checkout_details = {'product': [], 'total': [], 'amount': []}

    def checkout(self):
        self.cart_product = Cart.objects.filter(user=self.user)

        if not self.cart_items:
            return False

        self.calculate_cart_amount()
        self.prepare_checkout_details()

        return self.checkout_details

    
    def calculate_cart_amount(self):
        for cart_product in self.cart_items:
            self.cart_total_amount += cart_products.item.price * cart_products.quantity
   
    def prepare_checkout_details(self):
        for cart_product in self.cart_products:
            self.checkout_details['products'].append({
                                                      
                                                      'product_id': cart_products.item.id,
                                                      'product_name': cart_products.item.title,
                                                      'quantity': cart_products.quantity,
                                                      'price': cart_products.price})

        self.checkout_details['total'].append({'total_price': self.cart_base_total_amount})

        