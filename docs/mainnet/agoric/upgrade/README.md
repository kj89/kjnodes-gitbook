---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: agoric-3 | **Latest Version Tag**: pismoA | **Custom Port**: 27

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/agoric.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf agoric-sdk
git clone https://github.com/Agoric/agoric-sdk.git
cd agoric-sdk

# Build binaries
git checkout pismoA
make build
mkdir -p $HOME/.agoric/cosmovisor/upgrades/agoric-upgrade-8/bin
mv golang/cosmos/build/agd $HOME/.agoric/cosmovisor/upgrades/agoric-upgrade-8/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
