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
# Clone project repository
cd $HOME
rm -rf ${LATEST_VERSION_TAG}
git clone ${GIT_URL} ${LATEST_VERSION_TAG}
cd ${LATEST_VERSION_TAG}
git checkout ${LATEST_VERSION_TAG}

# Install and build Agoric Javascript packages
yarn install && yarn build

# Install and build Agoric Cosmos SDK support
(cd packages/cosmic-swingset && make)

# Prepare binaries for Cosmovisor
mkdir -p $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${LATEST_VERSION_NAME}/bin
ln -s $HOME/${LATEST_VERSION_TAG}/bin/agd $HOME/${CHAIN_DIR}/cosmovisor/upgrades/${LATEST_VERSION_NAME}/bin/agd
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
