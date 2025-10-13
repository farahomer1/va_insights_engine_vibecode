# va_insights_engine_vibecode
Vibecoded solution created through Firebase IDE

__Please run these commands on your Mac's terminal:__

__1. Navigate to the Project Folder:__ First, make sure you are in the correct directory.

```bash
cd ~/Downloads/va_insights_engine
```

__2. Delete the Old, Faulty Environment:__ It is crucial to start fresh.

```bash
rm -rf venv
```

__3. Create a New Virtual Environment:__

```bash
python3 -m venv venv
```

__4. Activate the New Environment:__

```bash
source venv/bin/activate
```

*(Your terminal prompt will now start with `(venv)`)*

__5. Upgrade Pip (Crucial Step):__ This command updates the package installer itself before we use it.

```bash
pip install --upgrade pip
```

__6. Install All Dependencies:__ Now that `pip` is up-to-date, it will correctly install all packages from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

__7. Run the Application:__

```bash
streamlit run app.py
```

This sequence ensures that all tools are up-to-date and all dependencies are installed correctly into a clean environment. The application will now launch successfully.
