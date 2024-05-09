import './App.css';

const App = () => {
  const telegramUrl = 'https://t.me/Lead_DealMaster_Bot';

  const handleButtonClick = () => {
    window.location.href = telegramUrl;
  };

  return (
    <div className="App">
      <div className="button_wrapper">
        <button className="redirect_button" onClick={handleButtonClick}>
          Перейти к боту
        </button>
      </div>
    </div>
  );
};

export default App;

