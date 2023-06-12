---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: agoric-emerynet-8 | **Latest Version Tag**: mainnet1B-rc3 | **Custom Port**: 127

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf mainnet1B-rc3
git clone https://github.com/Agoric/agoric-sdk.git mainnet1B-rc3
cd mainnet1B-rc3
git checkout mainnet1B-rc3

# Install and build Agoric Javascript packages
yarn install && yarn build

# Install and build Agoric Cosmos SDK support
(cd packages/cosmic-swingset && make)

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-10/bin
ln -s $HOME/mainnet1B-rc3/bin/agd $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-10/bin/agd
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
