---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/${PROJECT_NAME}.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: ${CHAIN_ID} | **Latest Version Tag**: ${LATEST_VERSION_TAG} | **Custom Port**: ${CHAIN_PORT}

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/${PROJECT_NAME}.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf ${GIT_DIR}
git clone ${GIT_URL}
cd ${GIT_DIR}

# Build binaries
git checkout ${LATEST_VERSION_TAG}
make build
mkdir -p $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${LATEST_VERSION_NAME}/bin
mv ${CHAIN_BINARY_SRC} $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${LATEST_VERSION_NAME}/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
