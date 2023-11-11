# Create requirements.in
```
touch requirements.in
```

# Install packages
```
pip3 install pip-tools
pip-compile
```

# Start backend server
```
uvicorn main:app --reload
```