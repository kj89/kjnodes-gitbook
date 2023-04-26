---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/${PROJECT_NAME}.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: ${CHAIN_ID} | **Latest Version Tag**: ${LATEST_VERSION_TAG} | **Custom Port**: ${CHAIN_PORT}

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Download project binaries
mkdir -p $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${LATEST_VERSION_NAME}/bin
wget -O $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${LATEST_VERSION_NAME}/bin/gravityd https://github.com/Gravity-Bridge/Gravity-Bridge/releases/download/${LATEST_VERSION_TAG}/gravity-linux-amd64
wget -O $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${LATEST_VERSION_NAME}/bin/gbt https://github.com/Gravity-Bridge/Gravity-Bridge/releases/download/${LATEST_VERSION_TAG}/gbt
chmod +x $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${LATEST_VERSION_NAME}/bin/*
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
