---
description: Prepare for and the upcomming chain upgrade using Cosmovisor.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/cosmos-images/main/logos/agoric.png" alt=""><figcaption></figcaption></figure>

**Chain ID**: agoric-emerynet-5 | **Latest Version Tag**: mainnet1B-rc0 | **Custom Port**: 127

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf mainnet1B-rc0
git clone https://github.com/Agoric/agoric-sdk.git mainnet1B-rc0
cd mainnet1B-rc0
git checkout mainnet1B-rc0

# Install and build Agoric Javascript packages
yarn install && yarn build

# Install and build Agoric Cosmos SDK support
(cd packages/cosmic-swingset && make)

# Prepare binaries for Cosmovisor
mkdir -p $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-10/bin
ln -s $HOME/mainnet1B-rc0/packages/cosmic-swingset/bin/ag-chain-cosmos $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-10/bin/ag-chain-cosmos
ln -s $HOME/mainnet1B-rc0/packages/cosmic-swingset/bin/ag-nchainz $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-10/bin/ag-nchainz
cp golang/cosmos/build/agd $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-10/bin/
cp golang/cosmos/build/ag-cosmos-helper $HOME/.agoric/cosmovisor/upgrades/agorictest-upgrade-10/bin/
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
