# API Stress Testing Tool

A simple async stress testing tool for chat completion APIs built with Python. This tool allows you to perform concurrent requests to test API performance and reliability.

## Features

- Configurable number of parallel requests
- Detailed performance metrics including:
  - Average response time
  - Minimum response time
  - Maximum response time
  - Standard deviation
  - Success/failure tracking
- Async implementation for efficient concurrent testing
- JSON payload customization support

## Prerequisites

- Python 3.7+
- pip (Python package installer)

## Installation

1. Clone this repository or download the source code:
```bash
git clone <your-repository-url>
cd <repository-directory>
```

2. Install the required dependency:
```bash
pip install aiohttp
```

## Usage

1. Make sure your API server is running and accessible at the configured endpoint (default: `http://localhost:11434/v1/chat/completions`)

2. Make the script executable:
```bash
chmod +x stress_test.py
```

3. Run the stress test:
```bash
python3 stress_test.py
```

### Customizing the Test

To modify the number of parallel requests:

1. Open the script in your preferred editor:
```bash
nano stress_test.py
```

2. Locate and modify the `N_REQUESTS` variable:
```python
N_REQUESTS = 10  # Change this number to your desired value
```

3. Save the file and run the test again.

## Configuration

The default configuration in the script includes:

- 10 parallel requests
- Default payload targeting a chat completion endpoint
- JSON payload using the qwen2.5:32b model
- Simple "Tell me a joke" prompt

You can customize the payload and endpoint by modifying the `PAYLOAD` and URL in the script.

## Output

The tool will display:
- Start time of the test
- Progress of individual requests
- Summary statistics including:
  - Average response time
  - Minimum response time
  - Maximum response time
  - Standard deviation
  - Number of successful/failed requests

## Error Handling

The script includes basic error handling and will:
- Track failed requests separately
- Continue running even if some requests fail
- Provide a summary of failed requests in the final report

## Contributing

Feel free to submit issues and enhancement requests!
