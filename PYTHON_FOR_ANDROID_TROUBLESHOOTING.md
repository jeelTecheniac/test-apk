# Python for Android Toolchain Troubleshooting Guide

## 🚨 **Error: pythonforandroid.toolchain create failed**

### **Error Description**

```
# Command failed: ['/opt/hostedtoolcache/Python/3.10.18/x64/bin/python', '-m', 'pythonforandroid.toolchain', 'create', '--dist_name=ambulancebooking', 'bootstrap=sd12', '--requirements=python3,kivy==2.1.0,kivymd==1.1.1,pillow,requests', '--arch=arm64-v8a', '--arch=armeabi-v7a', '--copy-libs', '--color=always', '--storage-dir=/home/runner/work/test-apk/test-apk/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a', '--ndk-api=21', '--ignore-setup-py', '--debug']
```

### **Root Cause**

This error occurs when:

- **python-for-android** package is not properly installed
- **Python path** is not correctly configured
- **Buildozer** cannot find the required toolchain
- **Dependencies** are missing or incompatible

### ✅ **Solutions Applied**

#### 1. **Enhanced Python Dependencies Installation**

```yaml
- name: Install Python dependencies
  run: |
    python -m pip install --upgrade pip
    pip install buildozer cython==0.29.33
    pip install kivy==2.1.0 kivymd==1.1.1 pillow requests

    # Install python-for-android dependencies
    pip install python-for-android
    pip install --upgrade setuptools wheel

    # Install additional build dependencies
    pip install --upgrade virtualenv
```

#### 2. **Python for Android Configuration Step**

```yaml
- name: Configure Python for Android
  run: |
    # Set environment variables for python-for-android
    export PYTHONPATH=$PYTHONPATH:$HOME/.local/lib/python3.10/site-packages
    export PATH=$PATH:$HOME/.local/bin

    # Verify python-for-android installation
    python -c "import pythonforandroid; print('python-for-android version:', pythonforandroid.__version__)"

    # Check buildozer configuration
    buildozer --version

    # List installed packages
    pip list | grep -E "(buildozer|python-for-android|kivy|cython)"
```

#### 3. **Enhanced Build Step**

```yaml
- name: Build with Buildozer
  run: |
    # Set environment variables for the build
    export ANDROID_HOME=$HOME/.buildozer/android/platform/android-sdk
    export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/31.0.0
    export PYTHONPATH=$PYTHONPATH:$HOME/.local/lib/python3.10/site-packages
    export PATH=$PATH:$HOME/.local/bin

    # Verify environment
    echo "ANDROID_HOME: $ANDROID_HOME"
    echo "PATH: $PATH"
    echo "PYTHONPATH: $PYTHONPATH"

    # Clean previous builds if they exist
    buildozer android clean || echo "No previous builds to clean"

    # Build the APK with verbose output
    buildozer android debug -v
```

#### 4. **Updated buildozer.spec**

```ini
# Python for Android settings
android.arch = arm64-v8a armeabi-v7a
android.allow_newer_python = True
```

### 🔧 **Manual Fixes (If Still Having Issues)**

#### **Option 1: Force Reinstall python-for-android**

```bash
pip uninstall python-for-android -y
pip install python-for-android --force-reinstall
```

#### **Option 2: Use Specific Version**

```bash
pip install python-for-android==2023.8.7
```

#### **Option 3: Install from Source**

```bash
git clone https://github.com/kivy/python-for-android.git
cd python-for-android
pip install -e .
```

#### **Option 4: Check Python Version Compatibility**

```bash
python --version
# Ensure you're using Python 3.10.x
```

### 📋 **Verification Steps**

After applying fixes:

1. **Check python-for-android installation**:

   ```bash
   python -c "import pythonforandroid; print(pythonforandroid.__version__)"
   ```

2. **Verify buildozer**:

   ```bash
   buildozer --version
   ```

3. **Check Python path**:

   ```bash
   python -c "import sys; print(sys.path)"
   ```

4. **List installed packages**:
   ```bash
   pip list | grep -E "(buildozer|python-for-android|kivy|cython)"
   ```

### 🚀 **Next Steps**

1. **Commit and Push Changes**:

   ```bash
   git add .
   git commit -m "Fix python-for-android toolchain issues"
   git push origin main
   ```

2. **Monitor New Workflow Run**:

   - Go to Actions tab
   - Watch the new "Build Android APK" run
   - Should now pass the python-for-android step

3. **If Still Failing**:
   - Check the new error messages
   - Apply additional fixes from this guide
   - Consider using alternative build methods

### 💡 **Prevention Tips**

- **Always install python-for-android** explicitly
- **Set proper PYTHONPATH** environment variables
- **Use compatible versions** of Python and dependencies
- **Clean builds** before rebuilding
- **Use verbose output** (`-v` flag) for debugging

---

**Note**: The fixes applied should resolve the python-for-android toolchain error. If you encounter different errors after this, please share the new error logs for further assistance.
