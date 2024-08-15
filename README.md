# Multisearch RAG App

## Screenshots



## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
The Multisearch RAG App provides the following features:
1. **Multi-Source Search**: Utilizes various APIs to search across different platforms.
2. **Wikipedia Search**: Retrieve information from Wikipedia.
3. **ArXiv Research Paper Search**: Find relevant academic papers.
4. **Google Places Search**: Get information about various locations.
5. **Google Lens Image Search**: Search using image queries.
6. **Google Drive Integration**: Search through your Google Drive (currently commented out).
7. **LLM-Powered Responses**: Uses Groq LLM to process and generate responses.
8. **Interactive Interface**: User-friendly interface built with Streamlit for seamless interaction.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7+
- Streamlit
- LangChain (including `langchain_community`, `langchain_groq`, `langchain_googledrive`)
- SERP API key
- Google Cloud API key

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AtharshKrishnamoorthy/Multi-Search-RAG.git
   cd Multi-Search-RAG

2. Install the required packages:
     ```bash
     pip install -r requirements_RAG.txt

3. Set up environmental variables:
   - Create a `.env` file in the project directory.
   - Add your API keys to the `.env` file

    ```bash
    SERP_API_KEY=your_serp_api_key
    GOOGLECLOUD_API_KEY=your_google_cloud_api_key

## Usage

To run the MultiSearch RAG app:
1. Navigate to the project directory.
2. Run the Streamlit app:
    ```bash
    streamlit run multisearch_rag.py
3. Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).

## Querying

1. Enter your queries in the chat input box.
2. The system will provide responses based on the information retrieved from various sources.

## Model Details

- LLM Model : The model used here is `llama3-70b-8192` from Groq

## Configuration

Ensure you have the required environment setup for running the app. Modify `multisearch_rag.py` as needed for additional configurations or to enable/disable specific search tools.

## Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the original branch: `git push origin feature-branch-name`.
5. Create a pull request.

Please update tests as appropriate and adhere to the project's coding standards.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

If you have any questions, feel free to reach out:

- Project Maintainer: Atharsh K
- Email: atharshkrishnamoorthy@gmail.com
- Project Link: [GitHub Repository](https://github.com/AtharshKrishnamoorthy/Multi-Search-RAG)
