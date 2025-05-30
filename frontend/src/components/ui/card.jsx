import React from "react";

export function Card({ children, className = "" }) {
  return (
    <div className={`rounded-2xl shadow p-4 bg-white ${className}`}>
      {children}
    </div>
  );
}

export function CardContent({ children, className = "" }) {
  return (
    <div className={`mt-2 text-sm text-gray-600 ${className}`}>
      {children}
    </div>
  );
}