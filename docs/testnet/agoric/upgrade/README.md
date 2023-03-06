---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: agoric-emerynet-5 | **Latest Version Tag**: pismoC | **Custom Port**: 27

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
mkdir -p $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-9/bin
ln -s $HOME/pismoC/packages/cosmic-swingset/bin/ag-chain-cosmos $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-9/bin/ag-chain-cosmos
ln -s $HOME/pismoC/packages/cosmic-swingset/bin/ag-nchainz $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-9/bin/ag-nchainz
cp golang/cosmos/build/agd $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-9/bin/
cp golang/cosmos/build/ag-cosmos-helper $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-9/bin/
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
