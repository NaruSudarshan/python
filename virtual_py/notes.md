1. have virtualenv installed:
   ```bash
   pip install virtualenv
   ```

2. create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. activate the virtual environment:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
    - On macOS/Linux:
      ```bash
        source .venv/bin/activate
        ```
    
5. create requirments.txt with:
   ```bash
   pip freeze > requirements.txt
   ```

4. install the required packages from requirements.txt:
   ```bash
    pip install -r requirements.txt
    ```
    
5. deactivate the virtual environment when done:
   ```bash
   deactivate
   ```
