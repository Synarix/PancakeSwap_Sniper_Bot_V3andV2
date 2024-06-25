#!/bin/bash

# Function to check the Node.js version
check_node_version() {
  NODE_VERSION=$(node -v 2>/dev/null)
  if [[ $NODE_VERSION == v18* ]]; then
    echo "Node.js version 18 is already installed."
    return 0
  else
    echo "Node.js version 18 is not installed."
    return 1
  fi
}

# Function to install Node.js version 18 using nvm
install_node() {
  echo "Installing Node.js version 18..."
  # Install nvm if not installed
  if ! command -v nvm &> /dev/null; then
    echo "nvm is not installed. Installing nvm..."
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
    export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
  fi

  # Install Node.js version 18 using nvm
  nvm install 18
  nvm use 18
  nvm alias default 18
  echo "Node.js version 18 installed."
}

# Function to install Hardhat
install_hardhat() {
  echo "Installing Hardhat..."
  npm install -g hardhat
  echo "Hardhat installed."
}

# Check if Node.js version 18 is installed
if ! check_node_version; then
  install_node
else
  # If nvm is already installed, ensure the correct version is used
  if command -v nvm &> /dev/null; then
    nvm use 18
  fi
fi

# Check if Hardhat is installed
if ! command -v hardhat &> /dev/null; then
  install_hardhat
fi

# Start the Hardhat node as administrator
echo "Starting Hardhat node..."
sudo npx hardhat node