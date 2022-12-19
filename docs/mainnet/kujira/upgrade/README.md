---
description: Setting up your validator node has never been so easy. Get your validator running in minutes by following step by step instructions.
---

# Upgrade

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

**Chain ID**: kaiyo-1 | **Latest Version Tag**: v0.7.1 | **Custom Port**: 13

<figure><img src="https://raw.githubusercontent.com/kj89/testnet_manuals/main/pingpub/logos/kujira.png" width="150" alt=""><figcaption></figcaption></figure>

{% hint style='info' %}
Since we are using Cosmovisor, it makes it very easy to prepare for upcomming upgrade.
You just have to build new binaries and move it into cosmovisor upgrades directory.
{% endhint %}

## Download and build upgrade binaries

```bash
# Clone project repository
cd $HOME
rm -rf core
git clone https://github.com/Team-Kujira/core.git
cd core

# Build binaries
git checkout v0.7.1
make build
mkdir -p $HOME/.kujira/cosmovisor/upgrades/v0.7.1/bin
mv build/kujirad $HOME/.kujira/cosmovisor/upgrades/v0.7.1/bin/
rm -rf build
```

*Thats it! Now when upgrade block height is reached, Cosmovisor will handle it automatically!*
