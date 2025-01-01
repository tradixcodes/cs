import React from 'react';
import { ShoppingCart, PlusCircle, UserCircle, Search } from 'lucide-react';

const CartPage = () => {
  const cartItems = [
    {
      id: 1,
      store: "Phone Palace Kenya",
      product: "iPhone 16 Pro Max",
      specs: ["8GB RAM", "1TB Internal Storage"],
      price: 1999,
      image: "/api/placeholder/200/200"
    },
    {
      id: 2,
      store: "Phone Palace Kenya",
      product: "iPhone 16 Pro Max",
      specs: ["8GB RAM", "1TB Internal Storage"],
      price: 1999,
      image: "/api/placeholder/200/200"
    }
  ];

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-br from-amber-50 to-blue-50">
      {/* Header */}
      <header className="p-4 bg-white border-b">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center justify-between w-full md:w-auto gap-4">
            <h1 className="text-2xl font-serif">
              Vend<span className="text-amber-500">ora</span>
            </h1>
            <div className="flex items-center gap-3 md:hidden">
              <ShoppingCart className="w-6 h-6" />
              <PlusCircle className="w-6 h-6" />
              <UserCircle className="w-6 h-6" />
            </div>
          </div>
          
          <div className="relative flex-1 max-w-xl w-full">
            <Search className="absolute left-3 top-2.5 w-5 h-5 text-gray-400" />
            <input 
              type="search"
              placeholder="Search"
              className="w-full pl-10 pr-4 py-2 border rounded-full"
            />
          </div>
          
          <div className="hidden md:flex items-center gap-6">
            <div className="flex items-center gap-1">
              <ShoppingCart className="w-6 h-6" />
              <span>Cart</span>
            </div>
            <div className="flex items-center gap-1">
              <PlusCircle className="w-6 h-6" />
              <span>Save</span>
            </div>
            <UserCircle className="w-6 h-6" />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 p-4">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-xl font-medium mb-6">Cart</h2>
          
          {/* Cart Items */}
          <div className="space-y-4 mb-6">
            {cartItems.map((item) => (
              <div 
                key={item.id}
                className="bg-white rounded-xl p-4 flex flex-col md:flex-row items-start md:items-center gap-4"
              >
                <img 
                  src={item.image} 
                  alt={item.product}
                  className="w-24 h-24 bg-gray-100 rounded-lg object-cover"
                />
                
                <div className="flex-1">
                  <h3 className="font-medium">{item.store}</h3>
                  <p className="text-lg">{item.product}</p>
                  <div className="space-y-1 mt-1">
                    {item.specs.map((spec, index) => (
                      <p key={index} className="text-sm text-gray-600">{spec}</p>
                    ))}
                  </div>
                </div>
                
                <div className="flex flex-col md:flex-row items-end md:items-center gap-4 w-full md:w-auto">
                  <p className="text-lg font-bold">Price: ${item.price}</p>
                  <div className="flex gap-2 w-full md:w-auto">
                    <button className="px-4 py-2 bg-gray-900 text-white rounded-lg flex-1 md:flex-none">
                      Remove
                    </button>
                    <button className="px-4 py-2 bg-amber-100 rounded-lg flex-1 md:flex-none">
                      Check Out
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* Total */}
          <div className="bg-white rounded-xl p-4 flex items-center justify-between">
            <p className="text-xl font-bold">
              Total: ${cartItems.reduce((acc, item) => acc + item.price, 0)}
            </p>
            <button className="px-6 py-2 bg-amber-100 rounded-lg">
              Check Out All
            </button>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-amber-50 p-8 mt-8">
        <div className="max-w-7xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8">
          <div>
            <h1 className="text-2xl font-serif mb-4">
              Vend<span className="text-amber-500">ora</span>
            </h1>
          </div>
          
          <div>
            <h3 className="font-medium mb-4">About Vendora</h3>
            <ul className="space-y-2 text-gray-600">
              <li>Reviews</li>
              <li>Customer Support</li>
            </ul>
          </div>
          
          <div>
            <h3 className="font-medium mb-4">Legal</h3>
            <ul className="space-y-2 text-gray-600">
              <li>Privacy Policy</li>
              <li>Terms of service</li>
              <li>Terms of use</li>
            </ul>
          </div>
          
          <div>
            <h3 className="font-medium mb-4">Find us on social</h3>
            <ul className="space-y-2 text-gray-600">
              <li>Facebook</li>
              <li>Instagram</li>
              <li>Twitter</li>
              <li>LinkedIn</li>
            </ul>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default CartPage;