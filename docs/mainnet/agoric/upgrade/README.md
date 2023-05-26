---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoC | **Custom Port**: 127

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf pismoC
git clone https://github.com/Agoric/agoric-sdk.git pismoC
cd pismoC
git checkout pismoC

# Install and build Agoric Javascript packages
yarn install && yarn build

# Install and build Agoric Cosmos SDK support
(cd packages/cosmic-swingset && make)

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.agoric/cosmovisor/upgrades/agoric-upgrade-9/bin
ln -s $HOME/pismoC/bin/agd $HOME/.agoric/cosmovisor/upgrades/agoric-upgrade-9/bin/agd
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
