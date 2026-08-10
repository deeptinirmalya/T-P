import React, { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import ProductDetails from "./pages/ProductDetails";
import Cart from "./pages/Cart";

function App() {
  // Load initial cart state from localStorage (optional persistence)
  const [cart, setCart] = useState(() => {
    try {
      const savedCart = localStorage.getItem("simple_shop_cart");
      return savedCart ? JSON.parse(savedCart) : [];
    } catch (e) {
      return [];
    }
  });

  // Save cart to localStorage whenever cart changes
  useEffect(() => {
    try {
      localStorage.setItem("simple_shop_cart", JSON.stringify(cart));
    } catch (e) {
      console.error("Failed to save cart to localStorage", e);
    }
  }, [cart]);

  const DELIVERY_CHARGE = 50;
  const GST_RATE = 0.18;

  const coupons = {
    SAVE10: 10,
    SAVE20: 20,
    BLACKFRIDAY: 30,
    WELCOME5: 5,
  };

  const validateCoupon = (couponCode) => {
    const normalized = couponCode.trim().toUpperCase();
    const discount = coupons[normalized];

    if (discount == null) {
      return {
        success: false,
        data: null,
        error: "Coupon code not found",
      };
    }

    return {
      success: true,
      data: discount,
      error: null,
    };
  };

  const calculateOrderSummary = (price, discountPercent) => {
    const discountAmount = discountPercent
      ? (price * discountPercent) / 100
      : 0;
    const subtotal = price - discountAmount + DELIVERY_CHARGE;
    const gstAmount = subtotal * GST_RATE;
    const finalTotal = subtotal + gstAmount;

    return {
      discountAmount,
      delivery: DELIVERY_CHARGE,
      gstAmount,
      finalTotal,
    };
  };

  // Add product to cart or increment quantity if already present
  const addToCart = async (product) => {
    const couponCode = window.prompt(
      "Enter coupon code (leave blank to skip):"
    );

    let discountPercent = 0;
    let couponLabel = "No coupon";
    let couponError = null;

    if (couponCode && couponCode.trim()) {
      const couponResponse = validateCoupon(couponCode.trim());
      if (couponResponse.success) {
        discountPercent = couponResponse.data || 0;
        couponLabel = `${couponCode.trim().toUpperCase()} (${discountPercent}% off)`;
      } else {
        couponError = couponResponse.error || "Coupon code not found";
        const proceedWithoutCoupon = window.confirm(
          `Coupon was not applied: ${couponError}.\n\n` +
            `Do you want to continue without a coupon?`
        );
        if (!proceedWithoutCoupon) {
          return;
        }
        couponLabel = "No coupon";
      }
    }

    const summary = calculateOrderSummary(product.price, discountPercent);
    const summaryMessage = `Product: ${product.title}\n` +
      `Price: $${product.price.toFixed(2)}\n` +
      `Coupon: ${couponLabel}\n` +
      `Discount: $${summary.discountAmount.toFixed(2)}\n` +
      `Delivery: $${summary.delivery.toFixed(2)}\n` +
      `GST (18%): $${summary.gstAmount.toFixed(2)}\n` +
      `Final total: $${summary.finalTotal.toFixed(2)}\n\n` +
      `Do you want to add this item to your cart?`;

    const confirmed = window.confirm(summaryMessage);
    if (!confirmed) {
      return;
    }

    setCart((prevCart) => {
      const existingItem = prevCart.find((item) => item.id === product.id);

      if (existingItem) {
        return prevCart.map((item) =>
          item.id === product.id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        );
      } else {
        return [
          ...prevCart,
          {
            id: product.id,
            title: product.title,
            price: product.price,
            thumbnail: product.thumbnail,
            quantity: 1,
          },
        ];
      }
    });
  };

  // Increase or decrease item quantity (removes if quantity reaches 0)
  const updateQuantity = (id, delta) => {
    setCart((prevCart) =>
      prevCart
        .map((item) => {
          if (item.id === id) {
            const newQty = item.quantity + delta;
            return newQty > 0 ? { ...item, quantity: newQty } : null;
          }
          return item;
        })
        .filter(Boolean)
    );
  };

  // Remove product completely from cart
  const removeFromCart = (id) => {
    setCart((prevCart) => prevCart.filter((item) => item.id !== id));
  };

  // Clear all items in cart
  const clearCart = () => {
    setCart([]);
  };

  return (
    <>
      <Navbar cart={cart} />
      <Routes>
        <Route path="/" element={<Home addToCart={addToCart} />} />
        <Route
          path="/product/:id"
          element={<ProductDetails addToCart={addToCart} />}
        />
        <Route
          path="/cart"
          element={
            <Cart
              cart={cart}
              updateQuantity={updateQuantity}
              removeFromCart={removeFromCart}
              clearCart={clearCart}
            />
          }
        />
      </Routes>
    </>
  );
}

export default App;
