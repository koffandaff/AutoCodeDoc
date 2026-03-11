from backend.app.ml.model import WeatherPredictor

def main():
    print("Testing ML Backend Code...")
    predictor = WeatherPredictor(model_path="dummy.pt")
    predictor.load_weights()
    forecast = predictor.predict(temperature_grid=[[1.0, 0.5], [0.8, -0.2]], humidity=85.0)
    print(f"Prediction Result: {forecast}")

if __name__ == "__main__":
    main()
