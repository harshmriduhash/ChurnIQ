import React, { useState } from 'react';

type ChurnForm = {
  age: string;
  subscription_months: string;
  login_freq: string;
};

export default function App() {
  const [form, setForm] = useState<ChurnForm>({
    age: '',
    subscription_months: '',
    login_freq: '',
  });
  const [result, setResult] = useState<number | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch('http://localhost:8000/predict_churn', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        age: Number(form.age),
        subscription_months: Number(form.subscription_months),
        login_freq: Number(form.login_freq),
      }),
    });
    const data = await response.json();
    setResult(data.churn_probability);
  };

  return (
    <div>
      <h2>Churn Predictor</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Age:
          <input name="age" value={form.age} onChange={handleChange} type="number" />
        </label>
        <br />
        <label>
          Subscription Months:
          <input name="subscription_months" value={form.subscription_months} onChange={handleChange} type="number" />
        </label>
        <br />
        <label>
          Login Frequency:
          <input name="login_freq" value={form.login_freq} onChange={handleChange} type="number" />
        </label>
        <br />
        <button type="submit">Predict</button>
      </form>
      {result !== null && (
        <div>
          <h4>Churn Probability: {result}</h4>
        </div>
      )}
    </div>
  );
}
