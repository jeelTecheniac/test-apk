# Ambulance Booking System - Android APK Build Guide

This project is a KivyMD-based Android application for ambulance booking. This guide will walk you through the complete process of building an APK file using GitHub Actions.

## 🚀 Quick Start - Build APK with GitHub Actions

### Prerequisites
- GitHub account
- Repository with the project code
- GitHub Actions enabled

### Step-by-Step Process

#### 1. **Push Your Code to GitHub**
```bash
git add .
git commit -m "Initial commit for APK build"
git push origin main
```

#### 2. **Monitor GitHub Actions**
- Go to your GitHub repository
- Click on the "Actions" tab
- You'll see the "Build Android APK" workflow running
- The workflow will automatically trigger on push to main/master branch

#### 3. **Download the APK**
- Once the workflow completes successfully:
  - Go to the workflow run details
  - Scroll down to "Artifacts"
  - Download the "android-apk" artifact
  - Extract the APK file

#### 4. **Install on Android Device**
- Enable "Unknown Sources" in Android settings
- Transfer the APK to your Android device
- Tap the APK file to install

## 🔧 Manual Build Process (Alternative)

If you prefer to build locally or troubleshoot:

### Local Build Requirements
- Python 3.10
- Buildozer
- Android SDK/NDK
- Java JDK 17

### Local Build Commands
```bash
# Install buildozer
pip install buildozer

# Initialize buildozer (if not already done)
buildozer init

# Build debug APK
buildozer android debug

# Build release APK
buildozer android release
```

## 📱 Project Features

- **Ambulance Booking Interface**: User-friendly form for booking requests
- **Location Services**: GPS integration for pickup and destination
- **Special Care Support**: Fields for medical requirements
- **Modern UI**: Material Design with KivyMD
- **Cross-platform**: Built with Kivy framework

## 🛠️ Technical Details

### Dependencies
- **Kivy**: 2.1.0
- **KivyMD**: 1.1.1
- **Python**: 3.10+
- **Android API**: 31 (Android 12)
- **Min API**: 21 (Android 5.0)

### Permissions
- Internet access
- Fine location access
- Coarse location access
- Phone call capability

## 📋 Workflow Details

The GitHub Actions workflow:
1. **Sets up Ubuntu environment** with Python 3.10
2. **Installs system dependencies** (Java, build tools, libraries)
3. **Installs Python packages** (Kivy, KivyMD, Buildozer)
4. **Builds the APK** using Buildozer
5. **Uploads artifacts** for download
6. **Creates releases** (if building from tags)

## 🚨 Troubleshooting

### Common Issues

1. **Build Fails**: Check the Actions logs for specific error messages
2. **APK Not Generated**: Verify all dependencies are correctly specified
3. **Installation Issues**: Ensure Android device supports the minimum API level (21)

### Debug Steps
- Check GitHub Actions logs for detailed error information
- Verify buildozer.spec configuration
- Ensure all required files are present in the repository

## 📞 Support

If you encounter issues:
1. Check the GitHub Actions logs first
2. Verify your buildozer.spec configuration
3. Ensure all dependencies are correctly specified
4. Check that your main.py file is properly formatted

## 🔄 Updating the App

To update the app:
1. Make your code changes
2. Update version in buildozer.spec if needed
3. Commit and push to GitHub
4. The workflow will automatically build a new APK

---

**Note**: The first build may take longer as it downloads and caches Android SDK/NDK components. Subsequent builds will be faster due to caching.
