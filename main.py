import google.generativeai as genai  # type: ignore
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    genai.configure()
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Say hello")
    print(response.text)


if __name__ == "__main__":
    main()
