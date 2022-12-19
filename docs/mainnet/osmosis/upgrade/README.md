---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: osmosis-1 | **Latest Version Tag**: v13.1.0 | **Custom Port**: 29

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/osmosis.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf osmosis
git clone https://github.com/osmosis-labs/osmosis.git
cd osmosis

# Build binaries
git checkout v13.1.0
make build
mkdir -p $HOME/.osmosisd/cosmovisor/upgrades/v13/bin
mv build/osmosisd $HOME/.osmosisd/cosmovisor/upgrades/v13/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
